#!/usr/bin/env python3
"""
tests/test_config.py - Test config values
"""

import os
from .. import config as c


def test_host_up():
    """Test HOST is a valid, up and running server
    """
    config = c.DevelopmentConfig
    r = os.system('ping -c 1 ' + config.HOST)
    assert r != 0, 'Host is down or incorrect'


def _test_user_agent(config):
    expected = 'Tinder/7.5.3 (iPhone; iOS 10.3.2; Scale/2.00)'
    actual = config.USER_AGENT
    assert expected == actual


def _test_config(config):
    """
    """
    expected = ''
    actual = config.FB_USERNAME
    assert expected == actual

    expected = ''
    actual = config.FB_PASSWORD
    assert expected == actual

    expected = ''
    actual = config.FB_TOKEN
    assert expected == actual

    expected = ''
    actual = config.FB_ID
    assert expected == actual

    expected = ''
    actual = config.TINDER_AUTH_TOKEN
    assert expected == actual


def test_development_config():
    """
    """
    #_test_user_agent(c.DevelopmentConfig)
    #_test_config(c.DevelopmentConfig)
    pass


def test_testing_config():
    """
    """
    #_test_user_agent(c.CIConfig)
    #_test_config(c.CIConfig)
    pass
