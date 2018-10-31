#!/usr/bin/env python3
"""
config.py -
"""

import os


class Config:
    """Default Configuration
    """

    # DO NOT CHANGE UNLESS YOU KNOW WHAT YOU'RE DOING
    # Device
    APP_NAME = 'Tinder'
    APP_VERSION = '7.5.3'
    OS_NAME = 'iOS'
    OS_VERSION = '10.3.2'
    OS_RELEASE = ''
    OS_PLATFORM = OS_NAME.lower()
    PHONE_MANUFACTURER = 'Apple'
    PHONE_DEVICE = 'iPhone'
    PHONE_MODEL = ''
    PHONE_DPI = ''
    PHONE_RESOLUTION = ''
    PHONE_CHIPSET = ''
    LANGUAGE = 'en-US'
    VERSION_CODE = 'Scale/2.00'

    # Host
    HOST = 'https://api.gotinder.com'

    # Header
    CONTENT_TYPE = 'application/json'
    ACCEPT = 'application/json'

    USER_AGENT_FORMAT = \
        '{app_name}/{app_version} ({device}; {os_name} {os_version}; {version_code})'
    USER_AGENT = USER_AGENT_FORMAT.format(**{
        'app_name': APP_NAME,
        'app_version': APP_VERSION,
        'os_name': OS_NAME,
        'os_version': OS_VERSION,
        'device': PHONE_DEVICE,
        'version_code': VERSION_CODE})

    # Facebook Credentials
    FB_AUTH_URL = 'https://www.facebook.com/v2.6/dialog/oauth?redirect_uri=fb464891386855067%3A%2F%2Fauthorize%2F&display=touch&state=%7B%22challenge%22%3A%22IUUkEUqIGud332lfu%252BMJhxL4Wlc%253D%22%2C%220_auth_logger_id%22%3A%2230F06532-A1B9-4B10-BB28-B29956C71AB1%22%2C%22com.facebook.sdk_client_state%22%3Atrue%2C%223_method%22%3A%22sfvc_auth%22%7D&scope=user_birthday%2Cuser_photos%2Cuser_education_history%2Cemail%2Cuser_relationship_details%2Cuser_friends%2Cuser_work_history%2Cuser_likes&response_type=token%2Csigned_request&default_audience=friends&return_scopes=true&auth_type=rerequest&client_id=464891386855067&ret=login&sdk=ios&logger_id=30F06532-A1B9-4B10-BB28-B29956C71AB1&ext=1470840777&hash=AeZqkIcf-NEW6vBd'
    FB_USERNAME = os.getenv('FB_USERNAME', None)
    FB_PASSWORD = os.getenv('FB_PASSWORD', None)
    FB_TOKEN = os.getenv('FB_TOKEN', None)
    FB_ID = os.getenv('FB_ID', None)

    # Tinder Credentials
    TINDER_AUTH_TOKEN = os.getenv('TINDER_AUTH_TOKEN', None)
