# coding=utf-8
'''
Tinder API python wrapper
~~~~~~~~~~~~~~~~~~~~~~~~~

Read `readme.md` and `Tinder API.ipnyb` for usage.

:license: MIT, see LICENSE for more details.
'''

import json
import requests

class Tinder_API(object):
    def __init__(self, host='https://api.gotinder.com', headers={}, api_token=None):
        self._auth_key = 'X-Auth-Token'
        self._not_authenticated_error = {'error': 'Please authenticate first.'}
        self.host = host
        self.headers = headers if headers != {} else {
            'app_version': '6.9.4',
            'platform': 'ios',
            'User-agent': 'Tinder/7.5.3 (iPhone; iOS 10.3.2; Scale/2.00)',
            'Accept': 'application/json',
            'content-type': 'application/json',
        }
        if api_token is not None:
            self.authenticate(api_token)


    # AUTHENTICATION METHODS

    def authenticate(self, api_token):
        '''
        Sets the authenticate header attribute.
        '''
        self.headers.update({self._auth_key: api_token})


    # SMS authentication

    def send_otp_code(self, phone_number):
        '''
        Request a one time password from Tinder via SMS.

        :param phone_number: the phone number to send the otp to.
        '''
        data = {'phone_number': phone_number}
        url = self.host + "/v2/auth/sms/send?auth_type=sms"
        r = requests.post(url, headers=self.headers, data=json.dumps(data), verify=False)
        return r.json().get("data", {}).get("sms_sent", False)


    def get_refresh_token(self, phone_number, otp_code):
        '''
        Gets the refresh token.

        :param phone_number: the user's phone number.

        :param otp_code: received by the user on the number provided.
        '''
        data = {'otp_code': otp_code, 'phone_number': phone_number}
        url = self.host + "/v2/auth/sms/validate?auth_type=sms"
        r = requests.post(url, headers=self.headers, data=json.dumps(data), verify=False)
        return r.json().get("data", {}).get("refresh_token", None)


    def get_api_token(self, refresh_token):
        '''
        Gets the API token from the refresh token. Will also authenticate.

        :param refresh_token: Refresh token obtained from :method:`get_refresh_token`.
        '''
        data = {'refresh_token': refresh_token }
        url = self.host + '/v2/auth/login/sms'
        r = requests.post(url, headers=self.headers, data=json.dumps(data), verify=False)
        api_token = r.json().get("data", {}).get("api_token", None)
        self.authenticate(api_token)
        return api_token


    # FB authentication

    def get_facebook_auth_token(self, facebook_auth_token, facebook_user_id):
        '''
        Get api_token using Facebook.

        :param facebook_auth_token: the Facebook auth token of the user to authenticate.

        :param facebook_user_id: the Facebook ID of the user to authenticate.
        '''
        url = self.host + '/auth'
        req = requests.post(url,
                            headers=self.headers,
                            data=json.dumps(
                                {'facebook_token': facebook_auth_token, 'facebook_id': facebook_user_id})
                            )
        try:
            token = req.json()['token']
            self.authenticate(token)
            return token
        except Exception as e:
            return {'error': 'Something went wrong. Sorry, but we could not authorize you.', 'exception': e}


    # APP FUNCTIONALITY

    def get_recommendations(self):
        '''
        Returns a list of users that you can swipe on.
        '''
        if self._auth_key not in self.headers:
            return self._not_authenticated_error
        try:
            url = self.host + '/user/recs'
            r = requests.get(url, headers=self.headers)
            return r.json()
        except Exception as e:
            return {'error': 'Something went wrong with getting recomendations.', 'exception': e}


    def get_updates(self, last_activity_date=''):
        '''
        Returns all updates since the given activity date.

        :param last_activity_date: The last activity date is defaulted at the beginning of time.
            Format: '2017-07-09T10:28:13.392Z'
        '''
        if self._auth_key not in self.headers:
            return self._not_authenticated_error
        try:
            url = self.host + '/updates'
            r = requests.post(url,
                            headers=self.headers,
                            data=json.dumps({'last_activity_date': last_activity_date}))
            return r.json()
        except Exception as e:
            return {'error': 'Something went wrong with getting updates.', 'exception': e}


    def get_self(self):
        '''
        Returns your own profile data
        '''
        if self._auth_key not in self.headers:
            return self._not_authenticated_error
        try:
            url = self.host + '/profile'
            r = requests.get(url, headers=self.headers)
            return r.json()
        except Exception as e:
            return {'error': 'Something went wrong. Could not get your data.', 'exception': e}


    def change_preferences(self, **kwargs):
        '''
        Changes your search preferences.

        :param kwargs: a dictionary - whose keys become separate keyword arguments and the values become values of these arguments.
            age_filter_min: 18..46
            age_filter_max: 22..55
            age_filter_min <= age_filter_max - 4
            gender: 0 == seeking males, 1 == seeking females
            distance_filter: 1..100
            discoverable: true | false
            {'photo_optimizer_enabled':false}
        
        example: change_preferences(age_filter_min=30, gender=0)
        '''
        if self._auth_key not in self.headers:
            return self._not_authenticated_error
        try:
            url = self.host + '/profile'
            r = requests.post(url, headers=self.headers, data=json.dumps(kwargs))
            return r.json()
        except Exception as e:
            return {'error': 'Something went wrong. Could not change your preferences.', 'exception': e}


    def get_meta(self):
        '''
        Returns meta data on yourself. Including the following keys:
        ['globals', 'client_resources', 'versions', 'purchases',
        'status', 'groups', 'products', 'rating', 'tutorials',
        'travel', 'notifications', 'user']
        '''
        if self._auth_key not in self.headers:
            return self._not_authenticated_error
        try:
            url = self.host + '/meta'
            r = requests.get(url, headers=self.headers)
            return r.json()
        except Exception as e:
            return {'error': 'Something went wrong. Could not get your metadata.', 'exception': e}

    def get_meta_v2(self):
        '''
        Returns meta data on yourself from V2 API. Including the following keys:
        ['account', 'client_resources', 'plus_screen', 'boost',
        'fast_match', 'top_picks', 'paywall', 'merchandising', 'places',
        'typing_indicator', 'profile', 'recs']
        '''
        if self._auth_key not in self.headers:
            return self._not_authenticated_error
        try:
            url = self.host + '/v2/meta'
            r = requests.get(url, headers=self.headers)
            return r.json()
        except Exception as e:
            return {'error': 'Something went wrong. Could not get your metadata.', 'exception': e}

    def update_location(self, lat, lon):
        '''
        Updates your location to the given float inputs.
        Note: Requires a passport / Tinder Plus.

        :param lat: latitude.

        :param lon: longitude.
        '''
        if self._auth_key not in self.headers:
            return self._not_authenticated_error
        try:
            url = self.host + '/passport/user/travel'
            r = requests.post(url, headers=self.headers, data=json.dumps({'lat': lat, 'lon': lon}))
            return r.json()
        except Exception as e:
            return {'error': 'Something went wrong. Could not update your location.', 'exception': e}

    def reset_real_location(self):
        '''
        Reset your real location.
        Note: Requires a passport / Tinder Plus.
        '''
        if self._auth_key not in self.headers:
            return self._not_authenticated_error
        try:
            url = self.host + '/passport/user/reset'
            r = requests.post(url, headers=self.headers)
            return r.json()
        except Exception as e:
            return {'error': 'Something went wrong. Could not update your location.', 'exception': e}


    def get_recs_v2(self):
        '''
        This works more consistently then the normal get_recommendations becuase it seeems to check new location.
        '''
        if self._auth_key not in self.headers:
            return self._not_authenticated_error
        try:
            url = self.host + '/v2/recs/core?locale=en-US'
            r = requests.get(url, headers=self.headers)
            return r.json()
        except Exception as e:
            return {'error': 'Something went wrong. Could not get your recommendations.', 'exception': e}

    def set_webprofileusername(self, username):
        '''
        Sets the username for the webprofile.

        :param username: string
            ex: https://www.gotinder.com/@YOURUSERNAME
        '''
        if self._auth_key not in self.headers:
            return self._not_authenticated_error
        try:
            url = self.host + '/profile/username'
            r = requests.put(url, headers=self.headers,
                            data=json.dumps({'username': username}))
            return r.json()
        except Exception as e:
            return {'error': 'Something went wrong. Could not set webprofile username.', 'exception': e}

    def reset_webprofileusername(self, username):
        '''
        Resets the username for the webprofile

        :param username: ?
        '''
        if self._auth_key not in self.headers:
            return self._not_authenticated_error
        try:
            url = self.host + '/profile/username'
            r = requests.delete(url, headers=self.headers)
            return r.json()
        except Exception as e:
            return {'error': 'Something went wrong. Could not delete webprofile username.', 'exception': e}

    def get_person(self, id):
        '''
        Gets a user's profile via their id

        :param id: ID of the user to find
        '''
        if self._auth_key not in self.headers:
            return self._not_authenticated_error
        try:
            url = self.host + '/user/%s' % id
            r = requests.get(url, headers=self.headers)
            return r.json()
        except Exception as e:
            return {'error': 'Something went wrong. Could not get that person.', 'exception': e}


    def send_msg(self, match_id, msg):
        '''
        Send a message to a match

        :param match_id: match

        :param msg: message to send
        '''
        if self._auth_key not in self.headers:
            return self._not_authenticated_error
        try:
            url = self.host + '/user/matches/%s' % match_id
            r = requests.post(url, headers=self.headers,
                            data=json.dumps({'message': msg}))
            return r.json()
        except Exception as e:
            return {'error': 'Something went wrong. Could not send your message.', 'exception': e}

    def unmatch(self, match_id):
        '''
        Unmatch someone

        :param match_id: person to unmatch
        '''
        if self._auth_key not in self.headers:
            return self._not_authenticated_error
        try:
            url = self.host + '/user/matches/%s' % match_id
            r = requests.delete(url, headers=self.headers)
            return r.json()
        except Exception as e:
            return {'error': 'Something went wrong. Could not unmatch person.', 'exception': e}

    def superlike(self, person_id):
        '''
        Superlike someone

        :param person_id: person to superlike
        '''
        if self._auth_key not in self.headers:
            return self._not_authenticated_error
        try:
            url = self.host + '/like/%s/super' % person_id
            r = requests.post(url, headers=self.headers)
            return r.json()
        except Exception as e:
            return {'error': 'Something went wrong. Could not superlike.', 'exception': e}


    def like(self, person_id):
        '''
        Like someone

        :param person_id: person to like
        '''
        if self._auth_key not in self.headers:
            return self._not_authenticated_error
        try:
            url = self.host + '/like/%s' % person_id
            r = requests.get(url, headers=self.headers)
            return r.json()
        except Exception as e:
            return {'error': 'Something went wrong. Could not like.', 'exception': e}


    def dislike(self, person_id):
        '''
        Dislike someone

        :param person_id: person to dislike
        '''
        if self._auth_key not in self.headers:
            return self._not_authenticated_error
        try:
            url = self.host + '/pass/%s' % person_id
            r = requests.get(url, headers=self.headers)
            return r.json()
        except Exception as e:
            return {'error': 'Something went wrong. Could not dislike.', 'exception': e}


    def report(self, person_id, cause, explanation=''):
        '''
        Report someone
        
        :param cause: There are three options for cause:
            0 : Other and requires an explanation
            1 : Feels like spam and no explanation
            4 : Inappropriate Photos and no explanation

        :param explanation: optional user comment
        '''
        if self._auth_key not in self.headers:
            return self._not_authenticated_error
        try:
            url = self.host + '/report/%s' % person_id
            r = requests.post(url, headers=self.headers, data={
                            'cause': cause, 'text': explanation})
            return r.json()
        except Exception as e:
            return {'error': 'Something went wrong. Could not report.', 'exception': e}


    def match_info(self, match_id):
        '''
        Get info from match

        :param match_id: ID of the match to get info about
        '''
        if self._auth_key not in self.headers:
            return self._not_authenticated_error
        try:
            url = self.host + '/matches/%s' % match_id
            r = requests.get(url, headers=self.headers)
            return r.json()
        except Exception as e:
            return {'error': 'Something went wrong. Could not get your match info.', 'exception': e}


    def matches(self, page_token=None):
        '''
        Get matches, in increments of roughly 60. Use the page token in the response to obtain the next set.

        :param page_token: Page offset. Obtained in this function's response.
        '''
        if self._auth_key not in self.headers:
            return self._not_authenticated_error
        try:
            url = self.host + '/v2/matches?count=60'
            if page_token is not None:
                url += '&page_token=%s' % page_token 
            r = requests.get(url, headers=self.headers)
            return r.json()
        except Exception as e:
            return {'error': 'Something went wrong. Could not get your match info.', 'exception': e}


    def fast_match_count(self):
        '''
        Get your match count. Returns a value between 0 and 99.
        '''
        if self._auth_key not in self.headers:
            return self._not_authenticated_error
        try:
            url = self.host + '/v2/fast-match/preview'
            r = requests.get(url, headers=self.headers)
            count = r.headers['fast-match-count']
            # image is in the response but its in hex..
            return count
        except Exception as e:
            return {'error': 'Something went wrong. Could not get your fast-match count.', 'exception': e}

    
    def fast_match_teasers(self):
        '''
        Get the non blurred thumbnail image shown in the messages-window (the one showing the likes you received).
        '''
        if self._auth_key not in self.headers:
            return self._not_authenticated_error
        try:
            url = self.host + '/v2/fast-match/teasers'
            r = requests.get(url, headers=self.headers)
            return r.json()
        except Exception as e:
            return {'error': 'Something went wrong. Could not get your fast-match count.', 'exception': e}


    def trending_gifs(self, limit=3):
        '''
        Get trending GIFs.

        :param limit: limit to the number of results.
        '''
        if self._auth_key not in self.headers:
            return self._not_authenticated_error
        try:
            url = self.host + '/giphy/trending?limit=%s' % limit
            r = requests.get(url, headers=self.headers)
            return r.json()
        except Exception as e:
            return {'error': 'Something went wrong. Could not get the trending gifs.', 'exception': e}


    def gif_query(self, query, limit=3):
        '''
        Search for GIFs.

        :param limit: limit to the number of results.
        '''
        if self._auth_key not in self.headers:
            return self._not_authenticated_error
        try:
            url = self.host + '/giphy/search?limit=%s&query=%s' % (limit, query)
            r = requests.get(url, headers=self.headers)
            return r.json()
        except Exception as e:
            return {'error': 'Something went wrong. Could not get your gifs.', 'exception': e}


    def custom_request(self, resource, http_verb='get', data={}):
        '''
        Allow calling any resource of the Tinder API.

        :param resource: resource (part of the link after host).

        :param data: data to be sent with the request

        :param http_verb: HTTP verb.
            Can be: get, head, post, patch, put, delete, options

        :return: response object
        '''
        if self._auth_key not in self.headers:
            return self._not_authenticated_error
        try:
            http_verb_functions={ 'get': requests.get, 'head': requests.head, 'post': requests.post, 'patch': requests.patch, 'put': requests.put, 'delete': requests.delete, 'options': requests.options }
            request_has_body={ 'get': False, 'head': False, 'post': True, 'patch': True, 'put': True, 'delete': True, 'options': False }

            http_verb = http_verb.lower()
            url = self.host + resource
            http_verb_function = http_verb_functions[http_verb.lower()]

            if not request_has_body[http_verb]:
                url += self.data_to_query_string(data)

            # call API and developer must figure out what to do with the response
            return http_verb_function(url, headers=self.headers, data=data)
        except Exception as e:
            return {'error': 'Something went wrong.', 'exception': e}


    def data_to_query_string(self, data):
        '''
        Converts a dict into a query string

        :param data: data to be included in a query string

        :return: query string
        '''
        if type(data) is dict and data is not {}:
            return '?' + '&'.join([f"{key}={value}" for key, value in data.items()])
        return ''