import requests
import random
import string
import uuid
from authgateway import *
import secrets
from pathlib import Path
import sys


class SMSAuthException(BaseException):
    pass


class TinderSMSAuth(object):

    def __init__(self, email=None):
        self.installid = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=11))
        self.session = requests.Session()
        self.session.headers.update({"user-agent": "Tinder Android Version 11.24.0"})
        self.url = "https://api.gotinder.com"
        self.funnelid = str(uuid.uuid4())
        self.appsessionid = str(uuid.uuid4())
        self.deviceid = secrets.token_hex(8)
        self.authtoken = None
        self.refreshtoken = None
        self.userid = None
        self.email = email
        self.phonenumber = None
        if Path("smstoken.txt").exists():
            print("smstoken.txt found, if you wish to auth again from scratch, delete smstoken.txt")
            with open("smstoken.txt", "r") as fh:
                tokens = fh.read()
                t = tokens.split(",")
                self.authtoken = t[0]
                self.refreshtoken = t[1]
                print("authToken found: " + self.authtoken)
        self.login()

    def _postloginreq(self, body, headers=None):
        if headers is not None:
            self.session.headers.update(headers)
        r = self.session.post(self.url + "/v3/auth/login", data=bytes(body))
        response = AuthGatewayResponse().parse(r.content).to_dict()
        return response

    def loginwrapper(self, body, seconds, headers=None):
        response = self._postloginreq(body, headers)
        print(response)
        if "validatePhoneOtpState" in response.keys() and response["validatePhoneOtpState"]["smsSent"]:
            otpresponse = input("OTP Response from SMS: ")
            if self.refreshtoken is not None:
                resp = PhoneOtp(phone=self.phonenumber, otp=otpresponse, refresh_token=self.refreshtoken)
            else:
                resp = PhoneOtp(phone=self.phonenumber, otp=otpresponse)
            messageresponse = AuthGatewayRequest(phone_otp=resp)
            seconds += random.uniform(30, 90)
            header_timer = {"app-session-time-elapsed": format(seconds, ".3f")}
            return self.loginwrapper(messageresponse, seconds, header_timer)
        elif "validateEmailOtpState" in response.keys() and response["validateEmailOtpState"]["emailSent"]:
            emailoptresponse = input("Check your email and input the verification code just sent to you: ")
            refreshtoken = response["validateEmailOtpState"]["refreshToken"]
            if self.email is None:
                self.email = input("Input your email: ")
            messageresponse = AuthGatewayRequest(email_otp=EmailOtp(otp=emailoptresponse, email=self.email, refresh_token=refreshtoken))
            seconds += random.uniform(30, 90)
            header_timer = {"app-session-time-elapsed": format(seconds, ".3f")}
            return self.loginwrapper(messageresponse, seconds, header_timer)
        elif "error" in response.keys() and response["error"]["message"] == 'INVALID_REFRESH_TOKEN':
            print("Refresh token error, restarting auth")
            phonenumber = input("phone number (starting with 1, numbers only): ")
            self.phonenumber = phonenumber
            messageresponse = AuthGatewayRequest(phone=Phone(phone=self.phonenumber))
            seconds += random.uniform(30, 90)
            header_timer = {"app-session-time-elapsed": format(seconds, ".3f")}
            return self.loginwrapper(messageresponse, seconds, header_timer)
        elif "loginResult" in response.keys() and "authToken" in response["loginResult"].keys():
            return response
        else:
            raise SMSAuthException

    def login(self):
        payload = {
                "device_id": self.installid,
                "experiments": ["default_login_token", "tinder_u_verification_method", "tinder_rules",
                                "user_interests_available"]
        }
        self.session.post(self.url + "/v2/buckets", json=payload)
        if self.refreshtoken is not None:
            print("Attempting to refresh auth token with saved refresh token")
            messageout = AuthGatewayRequest(refresh_auth=RefreshAuth(refresh_token=self.refreshtoken))
        else:
            phonenumber = input("phone number (starting with 1, numbers only): ")
            self.phonenumber = phonenumber
            messageout = AuthGatewayRequest(phone=Phone(phone=self.phonenumber))
        seconds = random.uniform(100, 250)
        headers = {
                'tinder-version': "11.24.0", 'install-id': self.installid,
                'user-agent': "Tinder Android Version 11.24.0", 'connection': "close",
                'platform-variant': "Google-Play", 'persistent-device-id': self.deviceid,
                'accept-encoding': "gzip, deflate", 'appsflyer-id': "1600144077225-7971032049730563486",
                'platform': "android", 'app-version': "4023", 'os-version': "25", 'app-session-id': self.appsessionid,
                'x-supported-image-formats': "webp", 'funnel-session-id': self.funnelid,
                'app-session-time-elapsed': format(seconds, ".3f"), 'accept-language': "en-US",
                'content-type': "application/x-protobuf"
        }
        response = self.loginwrapper(messageout, seconds, headers)
        self.refreshtoken = response["loginResult"]["refreshToken"]
        self.authtoken = response["loginResult"]["authToken"]
        self.session.headers.update({"X-AUTH-TOKEN": self.authtoken})
        with open("smstoken.txt", "w") as fh:
            fh.write(self.authtoken + "," + self.refreshtoken)
            print("Auth token saved to smstoken.txt")


if __name__ == '__main__':
    print("This script will use the sms login to obtain the auth token, which will be saved to smstoken.txt")
    if len(sys.argv) > 1:
        emailaddy = sys.argv[1]
    else:
        emailaddy = None
    TinderSMSAuth(email=emailaddy)