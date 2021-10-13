import sys
import string
import random
import secrets
import uuid
from typing import Any
from pathlib import Path

import requests

import tinder.v2 as v2
import tinder.v3.auth as auth
import tinder.v3.auth.authgateway as agw
from tinder.user import User

class SMSAuthException(auth.AuthException):
    pass

class SMSNotSent(SMSAuthException):
    pass

class SMSUser(User):

    def __init__(self, phone_number: str, email: str = None, token_fn: str = None) -> None:
        super().__init__()

        self._install_id = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=11))
        
        self._funnel_id = str(uuid.uuid4())
        self._app_session_id = str(uuid.uuid4())
        self._device_id = secrets.token_hex(8)
        self._phone_number = phone_number
        self._email = email

        self._auth_token: str = None
        self._refresh_token: str = None
        self._user_id: str = None

        self._session.headers.update({'user-agent': 'Tinder Android Version 11.24.0'})

        self.load_token(token_fn)

    def load_token(self, token_fn: str) -> None:
        token_fn = token_fn or self._phone_number + '_token.txt'
        
        token_file = Path(token_fn)
        if token_file.exists():
            print(f'[+] `{token_fn}` found.\n[+] If you wish to auth again from scratch, delete it.')
            with token_file.open() as fh:
                tokens = fh.read()
                auth_token, refresh_token = tokens.split(',')
                self._auth_token = auth_token
                self._refresh_token = refresh_token

    def save_token(self, token_fn: str = None) -> None:
        if self._auth_token is None or self._refresh_token is None:
            print('[!] Missing tokens to save.')
            return
        
        token_fn = token_fn or self._phone_number + '_token.txt'
        token_file = Path(token_fn)

        if token_file.exists():
            token_file.unlink()

        with token_file.open('w', encoding='utf-8') as fh:
            fh.write(self._auth_token + ',' + self._refresh_token)
            print(f'[+] Auth tokens saved to `{token_fn}`')

    def _post_login(self, body: agw.AuthGatewayRequest, headers: dict[str, Any] = None) -> agw.AuthGatewayResponse:
        if headers is not None:
            self._session.headers.update(headers)
        
        r = self._session.post(auth.LOGIN_EP, data=bytes(body))
        response = agw.AuthGatewayResponse().parse(r.content).to_dict()
        return response

    def _login_wrapper(self, body: agw.AuthGatewayRequest, seconds: int, headers: dict[str, Any] = None) -> dict[str, Any]:
        response = self._post_login(body, headers)
        message_response: Optionnal[agw.AuthGatewayRequest] = None
        
        if 'validatePhoneOtpState' in response:
            if not response['validatePhoneOtpState']['smsSent']:
                raise SMSNotSent

            otp_code = input('[?] OTP Response from SMS: ')
            otp = agw.PhoneOtp(phone=self._phone_number, otp=otp_code)
            message_response = agw.AuthGatewayRequest(phone_otp=otp)

        elif 'getPhoneState' in response:
            self._refresh_token = response['getPhoneState']['refreshToken']
            refresh_token = agw.RefreshAuth(refresh_token=self._refresh_token)
            message_response = agw.AuthGatewayRequest(refresh_auth=refresh_token)
            
        elif 'validateEmailOtpState' in response and response['validateEmailOtpState']['emailSent']:
            email_opt_code = input('[?] Check your email and input the verification code just sent to you: ')
            email_refresh_token = response['validateEmailOtpState']['refreshToken']

            if self._email is None:
                self._email = input('[?] Input your email: ')
            
            email_otp = agw.EmailOtp(otp=email_opt_code, email=self._email, refresh_token=email_refresh_token)
            message_response = agw.AuthGatewayRequest(email_otp=email_otp)

        elif 'getEmailState' in response:
            email_refresh_token = response['getEmailState']['refreshToken']
            if self.email is None:
                self.email = input('Input your email: ')
            email = agw.Email(email=self._email, refresh_token=email_refresh_token)
            message_response = agw.AuthGatewayRequest(email=email)
        
        elif 'error' in response and response['error']['message'] == 'INVALID_REFRESH_TOKEN':
            print('[!] Refresh token error, restarting auth.')
            self._phone_number = input('[?] Phone number (starting with 1, numbers only): ')
            phone = agw.Phone(phone=self._phone_number)
            message_response = agw.AuthGatewayRequest(phone=phone)

        elif 'error' in response:
            raise SMSAuthException(response['error']['message'])

        elif 'loginResult' in response and 'authToken' in response['loginResult']:
            return response
        
        if message_response is not None:
            seconds += random.uniform(30, 90)
            header_timer = {'app-session-time-elapsed': format(seconds, '.3f')}
            return self._login_wrapper(message_response, seconds, header_timer)
        
        raise SMSAuthException('Unknown error.')

    def login(self) -> None:
        payload = {
                'device_id': self._install_id,
                'experiments': ['default_login_token',
                                'tinder_u_verification_method',
                                'tinder_rules',
                                'user_interests_available']
        }
        self._session.post(v2.BUCKET_EP, json=payload)

        if self._refresh_token is not None:
            print('[+] Attempting to refresh auth token with saved refresh token.')
            initial_state = agw.GetInitialState(refresh_token=self._refresh_token)
            message_out = agw.AuthGatewayRequest(get_initial_state=initial_state)
        else:
            phone = agw.Phone(phone=self._phone_number)
            message_out = agw.AuthGatewayRequest(phone=phone)
        
        seconds = random.uniform(100, 250)
        headers = {
                'tinder-version': '12.6.0',
                'install-id': self._install_id,
                'user-agent': 'Tinder Android Version 12.6.0',
                'connection': 'close',
                'platform-variant': 'Google-Play',
                'persistent-device-id': self._device_id,
                'accept-encoding': 'gzip, deflate',
                'appsflyer-id': '1600144077225-7971032049730563486',
                'platform': 'android',
                'app-version': '4023',
                'os-version': '25',
                'app-session-id': self._app_session_id,
                'x-supported-image-formats': 'webp',
                'funnel-session-id': self._funnel_id,
                'app-session-time-elapsed': format(seconds, '.3f'),
                'accept-language': 'en-US',
                'content-type': 'application/x-protobuf'
        }
        response = self._login_wrapper(message_out, seconds, headers)

        self._refresh_token = response['loginResult']['refreshToken']
        self._auth_token = response['loginResult']['authToken']
        self._session.headers.update({'X-Auth-Token': self._auth_token})

        self._logged = True

        self.save_token()
