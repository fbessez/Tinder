#!/usr/bin/env python3
"""
endpoints.py - All the endpoints
"""
import requests

class Endpoints(object):
    """

    Endpoints:
    /auth
    /v2
    /meta
    /user
    /updates
    /matches
    /like
    /pass
    /profile
    /passport
    /report
    /giphy
    """

    def get_auth_token(self, fb_auth_token, fb_user_id):
        """Gets the Tinder Auth Token
        """

        endpoint = '/auth'
        params = {
            'facebook_token': fb_auth_token,
            'facebook_id': fb_user_id
        }
        res = self.post_request(endpoint, params)
        x_auth_token = res["token"]
        return x_auth_token

    def get_recs(self, locale=None):
        """This works more consistently then the normal get_recommendations becuase it seeems to check new location
        """
        if locale == None:
            locale = 'en-US'
        endpoint = '/v2/recs/core?locale={}'.format(locale)
        return self.get_request(endpoint)

    def all_matches(self):
        """
        """
        endpoint = '/v2/matches'
        return self.get_request(endpoint)

    def fast_match_info(self):
        """
        """
        count = None
        endpoint = '/v2/fast-match/preview'
        url = self.config.HOST + endpoint
        r = requests.get(url, headers=self.headers)
        count = r.headers['fast-match-count']
        # image is in the response but its in hex..
        if (r.status_code != 200):
            raise RequestError(path)
        return count

    def get_meta(self):
        """Returns meta data on yourself. Including the following keys:

        ['globals', 'client_resources', 'versions', 'purchases','status',
         'groups', 'products', 'rating', 'tutorials', 'travel', 
         'notifications', 'user']
        """
        endpoint = '/meta'
        return self.get_request(endpoint)

    def get_recommendations(self):
        """Returns a list of users that you can swipe on
        """
        endpoints = '/user/recs'
        return self.get_request(endpoints)

    def get_person(self, user_id):
        """Gets a user's profile via their id
        """
        endpoint = '/user/{}'.format(user_id)
        return self.get_request(endpoint)

    def send_msg(self, match_id, msg):
        """Message a matched user
        """
        endpoint = '/user/matches/%s' % match_id
        params = {
            "message": msg
        }
        return self.post_request(endpoint, params)

    def get_updates(self, last_activity_date=None):
        """Returns all updates since the given activity date.

        The last activity date is defaulted at the beginning of time.
        Format for last_activity_date: "2017-07-09T10:28:13.392Z"
        """
        endpoint = '/updates'
        if last_activity_date == None:
            return self.get_request(endpoint)
        params = {
            "last_activity_date": last_activity_date
        }
        return self.post_request(endpoint, params)

    def match_info(self, match_id):
        """
        """
        endpoint = '/matches/{}'.format(match_id)
        return self.get_request(endpoint)

    def superlike(self, person_id):
        """
        """
        endpoint = '/like/{}/super'.format(person_id)
        return self.post_request(endpoint)

    def like(self, person_id):
        """
        """
        endpoint = '/like/{}'.format(person_id)
        return self.get_request(endpoint)

    def dislike(self, person_id):
        """Pass a person
        """
        endpoint = '/pass/{}'.format(person_id)
        return self.get_request(endpoint)

    def get_profile(self):
        """Returns your own profile data
        """
        endpoint = '/profile'
        return self.get_request(endpoint)

    def change_preferences(self, **kwargs):
        """ex: change_preferences(age_filter_min=30, gender=0)
        kwargs: a dictionary - whose keys become separate keyword arguments and the values become values of these arguments
        age_filter_min: 18..46
        age_filter_max: 22..55
        age_filter_min <= age_filter_max - 4
        gender: 0 == seeking males, 1 == seeking females
        distance_filter: 1..100
        discoverable: true | false
        {"photo_optimizer_enabled":false}
        """
        endpoint = '/profile'
        return self.post_request(url, kwargs)

    def set_web_profile_username(self, username):
        """Sets the username for the webprofile: https://www.gotinder.com/@YOURUSERNAME
        """
        endpoint = '/profile/username'
        params = {
            "username": username
        }
        return self.put_request(endpoint, params)

    def reset_web_profile_username(self, username):
        """Resets the username for the webprofile
        """
        endpoint = '/profile/username'
        return self.delete_request(endpoint)

    def update_location(self, lat, lon):
        """Updates your location to the given float inputs
        Note: Requires a passport / Tinder Plus
        """
        endpoint = '/passport/user/travel'
        params = {
            "lat": lat,
            "lon": lon
        }
        return self.post_request(endpoint, params)

    def reset_real_location(self):
        """
        """
        endpoint = '/passport/user/reset'
        return self.post_request(endpoint)

    def report(self, person_id, cause, explanation=''):
        """There are three options for cause:
            0 : Other and requires an explanation
            1 : Feels like spam and no explanation
            4 : Inappropriate Photos and no explanation
        """
        endpoint = '/report/{}'.format(person_id)
        params = {
            "cause": cause,
            "text": explanation
        }
        return self.post_request(endpoint, params)

    def trending_gifs(self, limit=None):
        if limit == None:
            limit = 3
        endpoint = '/giphy/trending?limit={}'.format(limit)
        return self.get_request(endpoint)

    def gif_query(self, query, limit=None):
        if limit == None:
            limit = 3
        endpoint = '/giphy/search?limit={}&query={}'.format(limit, query)
        return self.get_request(endpoint)
