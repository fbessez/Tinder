from typing import Any

import tinder.v2 as v2
from tinder.user import User

class V3User(User):

    @User.need_logged
    def matches(self, page_token: str = None) -> list:
        url = v2.MATCHES + '?count=60' + (f'&page_token={page_token}' if page_token else '')
        r = self._session.get(url)
        response = r.json()

        if 'data' not in response or \
            'matches' not in response['data']:
            raise Exception

        matches = response['data']['matches']
        next_page_token = response['data'].get('next_page_token', None)
        return matches, next_page_token
    
    @property
    @User.need_logged
    def all_matches(self) -> list:
        matches = []
        next_page_token = ''

        while next_page_token is not None:
            next_matches, next_page_token = self.matches(next_page_token)
            matches += next_matches

        return matches