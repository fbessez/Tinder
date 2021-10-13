import tinder

class V2Exception(tinder.APIException):
    pass

URL = tinder.URL / 'v2'
BUCKET_EP = URL / 'buckets'
RECS_EP = URL / 'user' / 'recs'