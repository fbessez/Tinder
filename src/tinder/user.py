import requests

import tinder
from tinder.recs import Rec

class UserNotLoggedException(tinder.APIException):
    pass

class User:

    def __init__(self) -> None:
        self._logged = False
        self._session = requests.Session()

    def need_logged(func):
        def wrapper(self, *args, **kwargs):
            if not self._logged:
                raise UserNotLoggedException(f'The user need to be logged to call the function {func}')
            return func(self, *args, **kwargs)
        return wrapper

    @property
    def logged(self) -> bool:
        return self._logged

    @property
    @need_logged
    def recs(self) -> dict:
        r = self._session.get(tinder.RECS_EP)
        result = r.json()['results']
        recs = [
            Rec.create(infos)
            for infos in result
        ]
        return recs

    @need_logged
    def like(self, user_rec) -> dict:
        r = self._session.get(tinder.LIKE_EP / self.id)
        return r.json()

    @need_logged
    def like_all(self) -> None:
        for rec in self.recs:
            if rec.rec_type == 'user':
                print(rec.name)
                print(self.like(rec))
                print()

    def login(self) -> None:
        raise NotImplementedError