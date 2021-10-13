import tinder

class V3Exception(tinder.APIException):
    pass

URL = tinder.URL / 'v3'