import sys
import string
import random
import secrets
import uuid
from typing import Any
from pathlib import Path

import requests

import tinder.v2.auth as auth
from tinder.v2.user import V2User
from tinder import Url

class SMSAuthException(auth.AuthException):
    pass

class SMSNotSent(SMSAuthException):
    pass

class ValidationFailed(SMSAuthException):
    pass

class SMSUser(V2User):

    def __init__(self, phone_number: str, email: str = None, token_fn: str = None) -> None:
        super().__init__()

        self._phone_number = phone_number
        self._email = email

        self._auth_token: str = None
        self._refresh_token: str = None
        self._user_id: str = None

        self._session.headers.update(
            {'user-agent': 'Tinder/11.4.0 (iPhone; iOS 12.4.1; Scale/2.00)',
            'content-type': 'application/json'}
        )

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

    def _post_login(self, url: Url, payload: dict) -> dict:
        r = self._session.post(url, json=payload)
        response = r.json()

        if 'error' in response:
            raise SMSAuthException(response['error']['message'])

        return response

    def _get_otp(self) -> str:
        data = {'phone_number': self._phone_number}
        response = self._post_login(auth.CODE_REQUEST_EP, data)

        if not response['data']['sms_sent']:
            raise SMSNotSent

        otp_code = input('[?] OTP Response from SMS: ')
        return otp_code

    def _get_refresh_token(self, otp_code: str) -> str:
        data = {'otp_code': otp_code, 'phone_number': self._phone_number}
        response = self._post_login(auth.CODE_VALIDATE_EP, data)

        if not response['data']['validated']:
            raise ValidationFailed
        
        return response['data']['refresh_token']

    def _get_api_token(self) -> str:
        data = {'refresh_token': self._refresh_token}
        response = self._post_login(auth.TOKEN_EP, data)

        return response['data']['api_token']

    def login(self) -> None:
        otp_code = self._get_otp()
        self._refresh_token = self._get_refresh_token(otp_code)
        self._auth_token = self._get_api_token()

        self._session.headers.update({'X-Auth-Token': self._auth_token})

        self._logged = True

        self.save_token()
