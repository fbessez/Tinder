#!/usr/bin/env python3
"""
tests/test_endpoints.py - Test endpoints
"""

import vcr
from pytest import fixture
from ..client import Client
from .. import config as c


@fixture
def tinder_client():
    """Returns testing client
    """
    return Client(config=c.DevelopmentConfig)


@vcr.use_cassette('./tinder_api/tests/vcr_cassettes/recs.yml', filter_query_parameters=['X-Auth-Token'])
def test_recs(tinder_client):
    """Test get recommendations v2
    """
    response = tinder_client.get_recs()

    assert isinstance(response, dict)
    assert response.get('meta').get('status') == 200, 'Status code should be 200'
    assert len(response.get('data').get('results')) == 17, 'Should have 17 recommendations'
