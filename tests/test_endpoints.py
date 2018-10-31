#!/usr/bin/env python3
"""
tests/test_endpoints.py - Test endpoints
"""

import pytest
import vcr
from tinder_api.client import Client
from tinder_api.utils import FileUtils


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
    FileUtils.save_json_to_file(response, VCR_BASE_PATH + '/recs.json')

    assert isinstance(response, dict)
    assert response.get('meta').get('status') == 200, 'Status code should be 200'
    results_key = response.get('data').get('results')
    assert len(results_key) >= 1, 'Should return at least one recommendations'

    user = 1
    assert results_key[user].get('content_hash'), 'Should have a content_hash key'
    assert results_key[user].get('distance_mi'), 'Should have a distance_mi key'
    facebook_key = results_key[user].get('facebook')
    assert facebook_key, 'Should have a facebook key'
    #assert facebook_key.get('common_connections'), 'Should have a common_connections key'
    #assert facebook_key.get('common_interests'), 'Should have a common_interests key'
    #assert facebook_key.get('connection_count'), 'Should have a connection_count key'
    assert results_key[user].get('s_number'), 'Should have a s_number key'
    spotify_key = results_key[user].get('spotify')
    assert spotify_key, 'Should have a spotify key'
    #assert spotify_key.get('spotify_connected'), 'Should have a spotify_connected key'

    assert results_key[user].get('teaser'), 'Should have a teaser key'
    #assert results_key[user].get('teasers'), 'Should have a teasers key'
    assert results_key[user].get('type'), 'Should have a type key'

    user_key = results_key[user].get('user')
    assert user_key, 'Should have a user key'
    #assert user_key.get('_key')
