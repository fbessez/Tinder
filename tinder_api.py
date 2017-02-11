import json
from datetime import datetime

import requests

'''
the url to get your fb_auth
https://www.facebook.com/v2.6/dialog/oauth?redirect_uri=fb464891386855067%3A%2F%2Fauthorize%2F&display=touch&state=%7B%22challenge%22%3A%22IUUkEUqIGud332lfu%252BMJhxL4Wlc%253D%22%2C%220_auth_logger_id%22%3A%2230F06532-A1B9-4B10-BB28-B29956C71AB1%22%2C%22com.facebook.sdk_client_state%22%3Atrue%2C%223_method%22%3A%22sfvc_auth%22%7D&scope=user_birthday%2Cuser_photos%2Cuser_education_history%2Cemail%2Cuser_relationship_details%2Cuser_friends%2Cuser_work_history%2Cuser_likes&response_type=token%2Csigned_request&default_audience=friends&return_scopes=true&auth_type=rerequest&client_id=464891386855067&ret=login&sdk=ios&logger_id=30F06532-A1B9-4B10-BB28-B29956C71AB1&ext=1470840777&hash=AeZqkIcf-NEW6vBd


the url to get your fb_id
http://findmyfbid.com/

'''

def auth_token(fb_auth_token, fb_user_id):
    req = requests.post(
        'https://api.gotinder.com/auth',
        headers=headers,
        data=json.dumps({'facebook_token': fb_auth_token, 'facebook_id': fb_user_id})
      )
    try:
        return req.json()["token"]
    except:
        return "no"