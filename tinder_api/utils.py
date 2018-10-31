#!/usr/bin/env python3
"""
utils.py - Helper functions
"""
import os
import re
import robobrowser
import requests
import json
from .config import Config
from .errors import AuthenticationError


class FBUtils:

    @staticmethod
    def get_facebook_credentials(username, password):
        """
        """

        fb_access_token = FBUtils.get_fb_access_token(username, password)
        if fb_access_token == None:
            raise AuthenticationError('No FB Access Token')
        fb_id = FBUtils.get_fb_id(fb_access_token)
        if fb_id == None:
            raise AuthenticationError('No FB ID')
        return fb_access_token, fb_id

    @staticmethod
    def get_fb_access_token(email, password):
        access_token = None
        s = robobrowser.RoboBrowser(user_agent=Config.USER_AGENT, parser="lxml")
        s.open(Config.FB_AUTH_URL)
        f = s.get_form()
        f["pass"] = password
        f["email"] = email
        s.submit_form(f)
        f = s.get_form()
        try:
            s.submit_form(f, submit=f.submit_fields['__CONFIRM__'])
            access_token = re.search(
                r"access_token=([\w\d]+)", s.response.content.decode()).groups()[0]
        except Exception as e:
            raise AuthenticationError(
                "Access token could not be retrieved. Check your username and password:" + str(e))
        return access_token

    @staticmethod
    def detect_suspicious_activity_error(browser):
        """Facebook has flagged request as suspicious, thus locking account.

        See: https://github.com/fbessez/Tinder/issues/47
        """
        pass

    @staticmethod
    def get_fb_id(access_token):
        """Gets facebook ID from access token
        """
        req = requests.get(
            'https://graph.facebook.com/me?access_token=' + access_token)
        return req.json()["id"]


class FileUtils:

    @staticmethod
    def find_file(name):
        for root, dirs, files in os.walk('./'):
            if name in files:
                return os.path.join(root, name)

    @staticmethod
    def save_json_to_file(data, file):
        with open(file, 'w') as outfile:
            json.dump(data, outfile, indent=4, sort_keys=True)

if __name__ == '__main__':
    pass
