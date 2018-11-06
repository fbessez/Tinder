#!/usr/bin/env python3
"""
client.py - API Client
"""

import requests
import json

from tinder_api.config import Config
from tinder_api.utils import FBUtils
from tinder_api.errors import RequestError
from tinder_api.endpoints import Endpoints




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
            "Accept": Config.ACCEPT,
        }
        if username != None and password != None:
            self.login(username, password)

    def login(self, username, password):
        """
        """
        # Get Tinder auth token if needed
        if Config.TINDER_AUTH_TOKEN == None:
            # Get facebook token and id if needed
            if Config.FB_TOKEN == None or Config.FB_ID == None:
                # Get facebook username and password from params if needed
                if Config.FB_USERNAME == None or Config.FB_PASSWORD == None:
                    # Set username and password
                    Config.FB_USERNAME = username
                    Config.FB_PASSWORD = password
                # Set facebook token and id
                Config.FB_TOKEN, Config.FB_ID = FBUtils.get_facebook_credentials(
                    Config.FB_USERNAME, Config.FB_PASSWORD)
            # Set tinder auth token
            Config.TINDER_AUTH_TOKEN = self.get_auth_token(
                Config.FB_TOKEN, Config.FB_ID)
        self.headers.update({"X-Auth-Token": Config.TINDER_AUTH_TOKEN})

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
