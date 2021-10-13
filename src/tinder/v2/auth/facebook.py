

import sys
import string
import random
import secrets
import uuid
from typing import Any
from pathlib import Path

import requests
import robobrowser

import tinder.v2.auth as auth
from tinder.user import User


class FBAuthException(auth.AuthException):
    pass

class FBTokenException(auth.AuthException):
    pass

class FBIdException(auth.AuthException):
    pass


class FBUSer(User):

    def __init__(self, email: str, password: str) -> None:
        super().__init__()
        
        self._email = email
        self._password = password

    def _get_fb_token(self) -> str:
        USER_AGENT = 'Tinder/7.5.3 (iPhone; iOS 10.3.2; Scale/2.00)'

        session = robobrowser.RoboBrowser(user_agent=USER_AGENT, parser='lxml')
        session.open(auth.FB_AUTH)

        connection_form = session.get_form()
        connection_form['pass'] = self._password
        connection_form['email'] = self._email
        session.submit_form(connection_form)

        confirmation_form = session.get_form()
        try:
            submit_value = confirmation_form.submit_fields['__CONFIRM__']
            session.submit_form(confirmation_form, submit=submit_value)
            response = session.response.content.decode()
            access_token = re.search(
                r'access_token=([\w\d]+)', response).groups()[0]
            return access_token
        except requests.exceptions.InvalidSchema as browser_address:
            access_token = re.search(
                r'access_token=([\w\d]+)', str(browser_address)).groups()[0]
            return access_token
        except Exception as e:
            raise FBTokenException(f'Access token could not be retrieved. Check your username and password.\n{e}')

    def _get_fb_id(self, fb_token: str):
        try:
            r = requests.get(
                auth.FB_ID + f'?access_token={fb_token}')
            return r.json()['id']
        except Exception as e:
            raise FBIdException(f'An error occured while retrieving fb id.\n{e}')

    def login(self):
        fb_token = self._get_fb_token()
        fb_id = self._get_fb_id(fb_token)

        try:
            r = self._session.post(
                auth.LOGIN_FB_EP,
                data=json.dumps(
                    {'token': fb_token, 'facebook_id': fb_id}
                )
            )

            print(r.json())
            tinder_auth_token = r.json()['data']['api_token']
            self._session.headers.update({'X-Auth-Token': tinder_auth_token})
            self._logged = True
        except Exception as e:
            raise FBAuthException(f'An error occured while auth with fb.\n{e}')

