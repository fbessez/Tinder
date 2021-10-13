from __future__ import annotations

from urllib.parse import urlparse

class APIException(Exception):
    pass

class Url(str):

    def __new__(cls, *args, **kwargs):
        return str.__new__(cls, *args, **kwargs)

    def __truediv__(self, other_part: str = '') -> Url:
        url = self + '/' + other_part
        return Url(url)

URL = Url('https://api.gotinder.com')
RECS_EP = URL / 'user' / 'recs'
LIKE_EP = URL / 'like'