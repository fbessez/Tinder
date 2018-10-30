#!/usr/bin/env python3
"""
client.py - API Client
"""

import requests
import json
from . import config as c
from . import utils
from .errors import AuthenticationError
from .endpoints import Endpoints


class Client(Endpoints, object):
    """API Client"""

    def __init__(self, username=None, password=None, config=None):
        """
        """
        self.config = config
        self.headers = {
            'app_version': '6.9.4',
            'platform': self.config.OS_PLATFORM,
            "content-type": self.config.CONTENT_TYPE,
            "User-agent": self.config.USER_AGENT,
            "Accept": self.config.ACCEPT,
        }
        self.login(username, password)

    def login(self, username=None, password=None):
        """
        """
        # Get Tinder auth token if needed
        if self.config.TINDER_AUTH_TOKEN == '':
            # Get facebook token and id if needed
            if self.config.FB_TOKEN == '' or self.config.FB_ID == '':
                # Get facebook username and password from params if needed
                if self.config.FB_USERNAME == '' or self.config.FB_PASSWORD == '':
                    # Set username and password
                    self.config.FB_USERNAME = username
                    self.config.FB_PASSWORD = password
                # Set facebook token and id
                self.config.FB_TOKEN, self.config.FB_ID = utils.get_facebook_credentials(
                    self.config.FB_USERNAME, self.config.FB_PASSWORD)
            # Set tinder auth token
            self.config.TINDER_AUTH_TOKEN = self.get_auth_token(
                self.config.FB_TOKEN, self.config.FB_ID)
        self.headers.update({"X-Auth-Token": self.config.TINDER_AUTH_TOKEN})

    def get_request(self, path):
        """"""
        r = requests.get(self.config.HOST + path, headers=self.headers)
        if (r.status_code != 200):
            raise RequestError(path)
        return r.json()

    def post_request(self, path, params=None):
        """"""
        r = {}
        if params == None:
            r = requests.post(self.config.HOST + path, headers=self.headers)
        else:
            data = json.dumps(params)
            r = requests.post(self.config.HOST + path, headers=self.headers, data=data)
        if (r.status_code != 200):
            raise RequestError(path)
        return r.json()

    def put_request(self, path, params):
        """"""
        data = json.dumps(params)
        r = requests.put(self.config.HOST + path, headers=self.headers, data=data)
        if (r.status_code != 200):
            raise RequestError(path)
        return r.json()

    def delete_request(self, path):
        """"""
        r = requests.delete(self.config.HOST + path, headers=self.headers)
        if (r.status_code != 200):
            raise RequestError(path)
        return r.json()
