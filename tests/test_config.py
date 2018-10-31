#!/usr/bin/env python3
"""
tests/test_config.py - Test config values
"""

import os
from tinder_api.config import Config


def test_host_up():
    """Test HOST is a valid, up and running server
    """
    r = os.system('ping -c 1 ' + Config.HOST)
    assert r != 0, 'Host is down or incorrect'


def test_user_agent():
    expected = 'Tinder/7.5.3 (iPhone; iOS 10.3.2; Scale/2.00)'
    actual = Config.USER_AGENT
    assert expected == actual


def test_facebook_credential():
    """
    """
    expected = None
    actual = Config.FB_USERNAME
    assert expected == actual

    expected = None
    actual = Config.FB_PASSWORD
    assert expected == actual

    expected = None
    actual = Config.FB_TOKEN
    assert expected == actual

    expected = None
    actual = Config.FB_ID
    assert expected == actual


def test_tinder_credential():
    """
    """
    expected = None
    actual = Config.TINDER_AUTH_TOKEN
    assert expected == actual
