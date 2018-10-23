#!/usr/bin/env python3
"""
client.py - API Client
"""

import requests
import json
from .config import Config
from .utils import get_facebook_credentials
from .errors import AuthenticationError
from .endpoints import Endpoints


class Client(Endpoints, object):
    """API Client"""

    def __init__(self, username=None, password=None):
        """
        """
        self.headers = {
            'app_version': '6.9.4',
            'platform': Config.OS_PLATFORM,
            "content-type": Config.CONTENT_TYPE,
            "User-agent": Config.USER_AGENT,
            "Accept": "application/json",
        }
        self.login(username, password)

    def login(self, username, password):
        if Config.TINDER_AUTH_TOKEN != '':
            self.headers.update({"X-Auth-Token": Config.TINDER_AUTH_TOKEN})
        else:
            if username == None or password == None:
                username = Config.FB_USERNAME
                password = Config.FB_PASSWORD
            fb_auth_token, fb_user_id = get_facebook_credentials(username, password)
            tinder_auth_token = self.get_auth_token(fb_auth_token, fb_user_id)
            self.headers.update({"X-Auth-Token": tinder_auth_token})

    def get_request(self, path):
        """"""
        r = requests.get(Config.HOST + path, headers=self.headers)
        if (r.status_code != 200):
            raise RequestError(path)
        return r.json()

    def post_request(self, path, params=None):
        """"""
        r = {}
        if params == None:
            r = requests.post(Config.HOST + path, headers=self.headers)
        else:
            data = json.dumps(params)
            r = requests.post(Config.HOST + path, headers=self.headers, data=data)
        if (r.status_code != 200):
            raise RequestError(path)
        return r.json()

    def put_request(self, path, params):
        """"""
        data = json.dumps(params)
        r = requests.put(Config.HOST + path, headers=self.headers, data=data)
        if (r.status_code != 200):
            raise RequestError(path)
        return r.json()

    def delete_request(self, path):
        """"""
        r = requests.delete(Config.HOST + path, headers=self.headers)
        if (r.status_code != 200):
            raise RequestError(path)
        return r.json()
