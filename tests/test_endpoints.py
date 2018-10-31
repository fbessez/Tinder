#!/usr/bin/env python3
"""
tests/test_endpoints.py - Test endpoints
"""

import pytest
import vcr
from tinder_api.client import Client


@pytest.fixture
def tinder_client():
    """Returns testing client
    """
    return Client()

VCR_BASE_PATH = './tests/vcr_cassettes'


@vcr.use_cassette(VCR_BASE_PATH + '/recs.yml', filter_query_parameters=['X-Auth-Token'])
def test_recs(tinder_client):
    """Test get recommendations v2
    """
    response = tinder_client.get_recs()

    assert isinstance(response, dict)
    assert response.get('meta').get('status') == 200, 'Status code should be 200'
    assert len(response.get('data').get('results')) == 17, 'Should have 17 recommendations'
