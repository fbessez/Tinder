import requests
import random
import string
import uuid
from authgateway import *
import secrets
from pathlib import Path


class SMSAuthException(BaseException):
    pass


class TinderSMSAuth(object):

    def __init__(self, email=None):
        self.installid = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=11))
        self.session = requests.Session()
        self.session.headers.update({"user-agent": "Tinder Android Version 11.23.0"})
        self.url = "https://api.gotinder.com"
        self.funnelid = str(uuid.uuid4())
        self.appsessionid = str(uuid.uuid4())
        self.deviceid = secrets.token_hex(8)
        self.authtoken = None
        self.refreshtoken = None
        self.userid = None
        self.email = email
        if Path("smstoken.txt").exists():
            print("smstoken.txt found, if you wish to auth again, delete smstoken.txt")
            with open("smstoken.txt", "r") as fh:
                tokens = fh.read()
                t = tokens.split(",")
                self.authtoken = t[0]
                self.refreshtoken = t[1]
                print("authToken found: " + self.authtoken)
        else:
            self.login()

    def login(self):
        payload = {
                "device_id": self.installid,
                "experiments": ["default_login_token", "tinder_u_verification_method", "tinder_rules",
                                "user_interests_available"]
        }
        self.session.post(self.url + "/v2/buckets", json=payload)
        phonenumber = input("phone number (starting with 1, numbers only): ")
        messageout = AuthGatewayRequest(Phone(phone=phonenumber))
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
        self.session.headers.update(headers)
        r = self.session.post(self.url + "/v3/auth/login", data=bytes(messageout))
        response = AuthGatewayResponse().parse(r.content).to_dict()
        print(response)
        if "validatePhoneOtpState" in response.keys() and response["validatePhoneOtpState"]["smsSent"]:
            otpresponse = input("OTP Response from SMS: ")
            resp = PhoneOtp(phone=phonenumber, otp=otpresponse)
            messageresponse = bytes(AuthGatewayRequest(phone_otp=resp))
            self.session.headers.update({"app-session-time-elapsed": format(seconds + random.uniform(30, 90), ".3f")})
            r = self.session.post(self.url + "/v3/auth/login", data=messageresponse)
            response = AuthGatewayResponse().parse(r.content).to_dict()
            print(response)
            if "validateEmailOtpState" in response.keys():
                emailoptresponse = input("Check your email and input the verification code just sent to you: ")
                refreshtoken = response["validateEmailOtpState"]["refreshToken"]
                email = input("Input your email: ")
                resp = bytes(AuthGatewayRequest(
                    email_otp=EmailOtp(otp=emailoptresponse, email=email, refresh_token=refreshtoken)))
                r = self.session.post(self.url + "/v3/auth/login", data=resp)
                response = AuthGatewayResponse().parse(r.content).to_dict()
                print(response)
            if "loginResult" in response.keys() and "authToken" in response["loginResult"].keys():
                self.refreshtoken = response["loginResult"]["refreshToken"]
                self.authtoken = response["loginResult"]["authToken"]
                with open("smstoken.txt", "w") as fh:
                    fh.write(self.authtoken + "," + self.refreshtoken)
                return self.session.headers.update({"X-Auth-Token": self.authtoken})
            else:
                raise SMSAuthException
        else:
            raise SMSAuthException


if __name__ == '__main__':
    print("This script will use the sms login to obtain the auth token, which will be saved to smstoken.txt")
    TinderSMSAuth()