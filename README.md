# Tinder API Documentation - 2020

First off, I want to give a shoutout to [@rtt](https://gist.github.com/rtt/10403467#file-tinder-api-documentation-md) who initially posted the Tinder API Documentation that I found most of these endpoints on. I am writing this to provide a more up-to-date resource for working with the Tinder API.

**Note: This was updated in May 2020 so it might be outdated.**

## API Documentation

### Host and Protocol

| Host | Protocol |
|--|--|
| api.gotinder.com | SSL |

### Required Headers

| Header | Example | Notes |
|---|---|---|
| X-Auth-Token | See "How to get facebook_token" below |  |
| Content-type | application/json |  |
| User-agent | Tinder/7.5.3 (iPhone; iOS 10.3.2; Scale/2.00) |  |

### Known Endpoints

Note: All endpoints are concatenated to the host url

Note: All curls must be sent with the headers as well (the only exception is that the /auth call must not have the X-Auth-Token header)

[@SeanLF](https://github.com/SeanLF) found some API endpoints from the [main.js](https://tinder.com/static/build/chunks/main-04c2dfb832c46d4a6eec.js) and included them in `api_endpoints.json`

| Endpoint| Purpose| Data?| Method |
|--|--|--|--|
| /auth| For authenticating| {'facebook_token': INSERT_HERE, 'facebook_id': INSERT_HERE}| POST|
| /v2/auth/sms/send?auth_type=sms| Part 1 of SMS authentication (two-factor)| {'phone_number': string}| POST|
| /v2/auth/sms/validate?auth_type=sms| Part 2 of SMS authentication (two-factor)| {'otp_code': string, 'phone_number': string }| POST|
| /v2/auth/login/sms| Part 3 of SMS authentication (two-factor)| {'refresh_token': string}| POST|
| /user/recs| Get match recommendations| {}| GET|
| /v2/matches| Get your matches| query in link should have count=1-100 e.g: /v2/matches?count=50| GET|
| /user/matches/_id| Send Message to that id| {"message": TEXT GOES HERE}| POST|
| /user/matches/match_id| Unmatch person| {}| DELETE |
| /user/_id| Get a user's profile data| {}| GET|
| /user/ping| Change your location| {"lat": lat, "lon": lon}| POST|
| /updates| Get all updates since the given date -- inserting "" will give you all updates since creating a Tinder account (i.e. matches, messages sent, etc.) | {"last_activity_date": ""} Input a timestamp: '2017-03-25T20:58:00.404Z' for updates since that time.| POST|
| /profile| Get your own profile data| {}| GET|
| /profile| Change your search preferences| {"age_filter_min": age_filter_min, "gender_filter": gender_filter, "gender": gender, "age_filter_max": age_filter_max, "distance_filter": distance_filter} | POST|
| /profile| (Tinder Plus Only) hide/show age| {"hide_age":boolean}| POST|
| /profile| (Tinder Plus Only) hide/show distance| {"hide_distance":boolean}| POST|
| /profile| (Tinder Plus Only) hide/show ads| {"hide_ads":boolean}| POST|
| /profile| (Tinder Plus Only) Set Tinder Blend options to "Recent Activity": Shows more recently active users| {"blend":"recency"}| POST|
| /profile| (Tinder Plus Only) Set Tinder Blend options to "Optimal": Scientifically proven to get you more matches| {"blend":"optimal"}| POST|
| /profile| (Tinder Plus Only) Set discovery settings to only people who already liked you| {"discoverable_party":"liked"}| POST|
| /passport/user/travel| (Tinder Plus Only) Travel to coordinate| {"lat":lat,"lon":lon}| POST|
| /v1/activity/feed?direction=past&eventTypes=1023 | Get activity feed, including old and updated bios for comparison| {}| GET|
| /instagram/authorize| Auth Instagram| {}| GET|
| /v2/profile/spotify/| Get Spotify settings| {}| GET|
| /v2/profile/spotify/theme| Set Spotify song| {"id":song_id}| PUT|
| /profile/username| Change your webprofile username| {"username": username}| PUT|
| /profile/username| Reset your webprofile username| {}| DELETE |
| /meta| Get your own meta data (swipes left, people seen, etc..)| {}| GET|
| /v2/meta| Get your own meta data from V2 API (extra data like "top_picks" info)| {}| GET|
| /report/_id| Report someone --> There are only a few accepted causes... (see tinder_api.py for options)| {"cause": cause, "text": explanation}| POST|
| /like/_id| Like someone a.k.a swipe right| {}| GET|
| /pass/_id| Pass on someone a.k.a swipe left| {}| GET|
| /like/_id/super| ~Super Like~ someone a.k.a swipe up| {}| POST|
| /matches/{match id}| Get a match from its id (thanks [@jtabet](https://github.com/jtabet) )| {}| GET|
| /message/{message id}| Get a message from its id (thanks [@jtabet](https://github.com/jtabet) )| {}| GET|
| /passport/user/reset| Reset your location to your real location| {}| POST|
| /passport/user/travel| Change your swiping location| {"lat": latitutde, "lon": longitude}| POST|
| /user/{user_id}/common_connections| Get common connection of a user| {}| GET|
| /profile/job| Set job| {"company":{"id":"17767109610","name":"University of Miami","displayed":true},"title":{"id":"106123522751852","name":"Research Assistant","displayed":true}}| PUT|
| /profile/job| Delete job| {}| DELETE |
| /profile/school| Set school(s)| {"schools":[{"id":school_id}]}| PUT|
| /profile/school| Reset school| {}| DELETE |
| /message/{message_id}/like| Like a message| {}| POST|
| /v2/fast-match/teasers| Get the non blurred thumbnail image shown in the messages-window (the one showing the likes you received)| {}| GET|
| /v2/fast-match/count| Get the number of likes you received| {}| GET|
| /giphy/trending?limit={limit}| Get the trending gifs (tinder uses giphy) accessible in chat| {}| GET|
| /giphy/search?limit={limit}&query={query}| Get gifs (tinder uses giphy) based on a search accessible in chat| {}| GET|

### Status Codes

|Status Code|Explanation|
|--|--|
|200|Everything went okay, and returned a result (if any).|
|301|The server is redirecting you to a different endpoint. This can happen when a company switches domain names, or an endpoint's name has changed.|
|400|The server thinks you made a bad request. This can happen when you don't send the information the API requires to process your request, among other things.|
|401|The server thinks you're not authenticated. This happens when you don't send the right credentials to access an API.|
|404|The server didn't find the resource you tried to access.|
|503|Back-end server is at capacity.|


## Library documentation

### ~~Config File~~

[@SeanLF](https://github.com/SeanLF) has removed the use of the config file after refactoring this library to use the Tinder_API class.

### Tinder_API usage

`tinder-api.py` contains a class called Tinder_API that provides a python wrapper for the Tinder API.

You may also look at the jupyter notebook (`Tinder API.ipynb`) for more code. Thanks to [@GloriaMacia](https://github.com/gloriamacia) and [@SeanLF](https://github.com/SeanLF) for making this possible.

#### Optional parameter when instantiating Tinder_API

- `host`: defaults to `https://api.gotinder.com`.
- `api_token`: specify if you have it already.

#### Authenticating with Facebook

Use the `facebook_auth_token.py` module to obtain Facebook credentials. Built with the help of [@PhillipeRemy](https://github.com/philipperemy/Deep-Learning-Tinder/blob/master/tinder_token.py)

```python
from tinder_api import Tinder_API
from tinder_api import facebook_auth_token

# User provides facebook_username & facebook_password.
facebook_auth_token = facebook_auth_token.get_facebook_access_token(facebook_username, facebook_password)
facebook_user_id = facebook_auth_token.get_facebook_id(facebook_access_token)
tinder_api = Tinder_API()
tinder_api.get_facebook_auth_token(facebook_auth_token, facebook_user_id)
# You can now call the API.
```

#### SMS Authentication

As opposed to Facebook auth, there's a rate limit to the number of SMS you can receive in an hour (supposedly 60).
Therefore, it is better to get your token once and use it within its 24 hour lifetime rather than asking for a new one everytime.
(implemented by [@Tagge](https://github.com/Tagge))

```python
from tinder_api import Tinder_API

tinder_api = Tinder_API()
# User provides the phone number.
tinder_api.send_otp_code(phone_number)
# User receives and provides OTP code.
refresh_token = tinder_api.get_refresh_token(phone_number, otp_code)
# Obtain an api_token valid for 24 hours.
api_token = tinder_api.get_api_token(refresh_token)
# You can now call the API.

# When api_token expires, call with the refresh token you have hopefully stored somewhere.
api_token = tinder_api.get_api_token(refresh_token)
# You can now call the API.
```

##### If you already have an API token stored

```python
from tinder_api import Tinder_API

# stored_api_token could be stored in a web session object.
tinder_api = Tinder_API(api_token=stored_api_token)
```

### Helper functions

See the documentation in `helpers.py` for more information, in particular for parameter and return documentation.

```python
def get_match_info(matches): # Wrap API data to python object for manipulation by helpers.

def get_match_id_by_name(match_info, name): # Returns a list of IDs that have the same requested name.

def get_photos(person): # Get a person's photos.

def calculate_age(birth_date_string): # Converts birthday string to age.

def sort_by_value(match_info, sort_type): # Sorts matches by the type requested.

def pause(): # In order to appear as a real Tinder user using the app...
             # When making many API calls, it is important to pause a...
             # realistic amount of time between actions to not make Tinder...
             # suspicious!
```
