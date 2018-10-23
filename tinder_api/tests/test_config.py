#!/usr/bin/env python3
"""
tests/test_config.py - Test config values
"""

import os

from ..config import Config


def test_host_up():
    """HOST is an up and running
    """
    r = os.system('ping -c 1 ' + Config.HOST)
    assert r != 0, 'Host is down or incorrect'
