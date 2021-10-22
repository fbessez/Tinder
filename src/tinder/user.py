from functools import reduce, wraps
from typing import Any

import requests

import tinder
from tinder.recs import Rec, TimeOutException, RetryException

class UserNotLoggedException(tinder.APIException):
    pass

class UnknownError(tinder.APIException):
    
    def __init__(self, message: str = ''):
        self.message = f'An unknow error as occured.\n{str(message)}'
        super().__init__(self.message)


class User:

    def __init__(self) -> None:
        self._logged = False
        self._session = requests.Session()

    def need_logged(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            if not self._logged:
                raise UserNotLoggedException(f'The user need to be logged to call the function {func}')
            return func(self, *args, **kwargs)
        return wrapper

    def make_request(url):
        def inner_deco(func):
            @wraps(func)
            def wrapper(self, *params, **kwargs):
                complete_url = reduce(lambda a, b: a / b, [url, *params])
                r = self._session.get(complete_url)
                response = r.json()
                return func(self, response, **kwargs)
            return wrapper
        return inner_deco

    @property
    def logged(self) -> bool:
        return self._logged

    @property
    @need_logged
    @make_request(tinder.RECS_EP)
    def recs(self, response: dict[str, Any]) -> list[Rec]:
        if 'message' in response:
            message = response['message']
            if message == 'recs timeout':
                raise TimeOutException
            elif message == 'retry required':
                raise RetryException

        if 'results' not in response:
            raise UnknownError(response)
        
        result = response['results']
        recs = [
            Rec.create(infos)
            for infos in result
        ]
        return recs

    @need_logged
    @make_request(tinder.LIKE_EP)
    def like(self, response: dict[str, Any]) -> tuple[bool, int]:
        match = response['match']
        like_remaining = response['likes_remaining']
        return match, like_remaining

    def login(self) -> None:
        raise NotImplementedError