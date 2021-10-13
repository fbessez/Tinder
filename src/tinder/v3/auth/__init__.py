import tinder.v3

class AuthException(tinder.v3.V3Exception):
    pass

URL = tinder.v3.URL / 'auth'
LOGIN_EP = URL / 'login'