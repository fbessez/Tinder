import requests
import json

CODE_REQUEST_URL = "https://api.gotinder.com/v2/auth/sms/send?auth_type=sms"
CODE_VALIDATE_URL = "https://api.gotinder.com/v2/auth/sms/validate?auth_type=sms"
TOKEN_URL = "https://api.gotinder.com/v2/auth/login/sms"

HEADERS = {'user-agent': 'Tinder/11.4.0 (iPhone; iOS 12.4.1; Scale/2.00)', 'content-type': 'application/json'}

def send_otp_code(phone_number):
    data = {'phone_number': phone_number}
    r = requests.post(CODE_REQUEST_URL, headers=HEADERS, data=json.dumps(data), verify=False)
    print(r.url)
    response = r.json()
    if(response.get("data")['sms_sent'] == False):
        return False
    else:
        return True

def get_refresh_token(otp_code, phone_number):
    data = {'otp_code': otp_code, 'phone_number': phone_number}
    r = requests.post(CODE_VALIDATE_URL, headers=HEADERS, data=json.dumps(data), verify=False)
    print(r.url)
    response = r.json()
    if(response.get("data")["validated"] == False):
        return False
    else:
        return response.get("data")["refresh_token"]
    
def get_api_token(refresh_token):
    data = {'refresh_token': refresh_token }
    r = requests.post(TOKEN_URL, headers=HEADERS, data=json.dumps(data), verify=False)
    print(r.url)
    response = r.json()
    return response.get("data")["api_token"]

phone_number = input("Please enter your phone number under the international format (country code + number): ")
log_code = send_otp_code(phone_number)
otp_code = input("Please enter the code you've received by sms: ")
refresh_token = get_refresh_token(otp_code, phone_number)
print("Here is your Tinder token: " + str(get_api_token(refresh_token)))