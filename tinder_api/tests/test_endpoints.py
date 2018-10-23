#!/usr/bin/env python3
"""
tests/test_endpoints.py - Test endpoints
"""

import os
import simplejson
from ..client import Client
from ..utils import save_json_to_file


def test_get_recs():
    """Test get recommendations v2

    """
