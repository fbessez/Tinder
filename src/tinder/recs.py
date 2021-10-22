from typing import Any

import tinder

class TimeOutException(tinder.APIException):
    
    def __init__(self):
        super().__init__('Time out while trying to get recs. Could be because there is no more.')


class RetryException(tinder.APIException):
    
    def __init__(self):
        super().__init__('Failed to retrieve recs. Retry needed.')

class Rec:

    _subclasses = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls._subclasses[cls._TYPE] = cls

    def __init__(self, infos: dict[str, Any]) -> None:
        self._infos = infos

    @classmethod
    def create(cls, infos: dict[str, Any]) -> Any:
        rec_type = infos['type']
        if rec_type not in cls._subclasses:
            return Rec(infos)
        
        return cls._subclasses[rec_type](infos[rec_type])

    @property
    def rec_type(self) -> str:
        return self._infos['type']


class UserRec(Rec):

    _TYPE = 'user'

    @property
    def rec_type(self) -> str:
        return self._TYPE

    @property
    def infos(self) -> dict:
        return self._infos

    @property
    def name(self) -> str:
        return self._infos['name']
    
    @property
    def bio(self) -> str:
        return self._infos['bio']

    @property
    def id(self) -> str:
        return self._infos['_id']
