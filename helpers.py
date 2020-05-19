# coding=utf-8
'''
This file collects important data on your matches,
allows you to sort them by last_activity_date, age,
gender, message count, and their average successRate.
'''

from datetime import date, datetime
from random import random
from time import sleep

import config

def get_match_info(matches):
    '''
    Wrap API data to python object for manipulation by helpers.

    :param matches: matches obtained from Tinder API.

    :return: `dict`
        key: person ID
        value: `dict`
            keys: name, match_id, message_count, photos, bio, gender, avg_success_rate, messages, age, distance, last_activity_date
    '''
    match_info = {}
    for match in matches[:len(matches)]:
        try:
            person = match['person']
            person_id = person['_id']  # This ID for looking up person
            match_info[person_id] = {
                'name': person['name'],
                'match_id': match['id'],  # This ID for messaging
                'message_count': match['message_count'],
                'photos': get_photos(person),
                'bio': person['bio'],
                'gender': person['gender'],
                'avg_success_rate': get_avg_success_rate(person),
                'messages': match['messages'],
                'age': calculate_age(match['person']['birth_date']),
                'distance': person['distance_mi'], # in miles
                'last_activity_date': match['last_activity_date'],
            }
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
    return match_info


def get_match_id_by_name(match_info, name):
    '''
    Returns a list of IDs that have the same requested name.

    :param match_info: value from calling :method: `get_match_info`.

    :param name: whose name to look for.

    :return: list of IDs that have the same requested name.
    '''
    list_of_ids = []
    for match in match_info:
        if match_info[match]['name'] == name:
            list_of_ids.append(match_info[match]['match_id'])
    if len(list_of_ids) > 0:
        return list_of_ids
    return {'error': "No matches by name of %s" % name}


def get_photos(person):
    '''
    Get a person's photos.

    :param person: whose photos to get.

    :return: list of photo urls.
    '''
    photos = person['photos']
    photo_urls = []
    for photo in photos:
        photo_urls.append(photo['url'])
    return photo_urls


def calculate_age(birth_date_string):
    '''
    Converts birthday string to age.

    :param birth_date_string: string from person profile.
        ex: '1997-03-25T22:49:41.151Z'
    
    :return: age.
    '''
    birth_year = int(birth_date_string[:4])
    birth_month = int(birth_date_string[5:7])
    birth_day = int(birth_date_string[8:10])
    today = date.today()
    return today.year - birth_year - ((today.month, today.day) < (birth_month, birth_day))


def get_avg_success_rate(person):
    '''
    Success Rate is determined by Tinder for their 'Smart Photos' feature

    :param person: whose success rate are you requesting?

    :return: average success rate.
    '''
    photos = person['photos']
    curr_avg = 0
    for photo in photos:
        try:
            photo_successRate = photo['successRate']
            curr_avg += photo_successRate
        except:
            return -1
    return curr_avg / len(photos)


def sort_by_value(match_info, sort_type):
    '''
    Sorts matches by the type requested.

    :param match_info: value from calling :method: `get_match_info`.

    :param sort_type: one of: 'age', 'message_count', 'gender'.
    '''
    return sorted(match_info.items(), key=lambda x: x[1][sort_type], reverse=True)


def how_long_in_words(duration, include_seconds=False):
    '''
    Converts a datetime difference into words.

    :param duration: datetime difference.

    :param include_seconds: whether to include seconds or not.

    :return: duration in words.
    '''
    secs = duration.seconds
    days = duration.days
    m, s = divmod(secs, 60)
    h, m = divmod(m, 60)
    how_long = ("%d days, %d hrs %02d min" % (days, h, m))
    if include_seconds:
        how_long = ("%s %02d s" % (how_long, s))
    return how_long


def how_long_in_words_since(ping_time):
    '''
    How long since a person was seen on Tinder.

    :return: duration formatted as a `string`.
    '''
    ping_time = ping_time[:len(ping_time) - 5]
    datetime_ping = datetime.strptime(ping_time, '%Y-%m-%dT%H:%M:%S')
    return how_long_in_words(datetime.utcnow() - datetime_ping)


def how_long_since_last_seen(person):
    '''
    How long since a person was seen on Tinder.

    :return: duration formatted as a `string`.
    '''
    return how_long_in_words_since(person['last_activity_date'])


def how_long_since_last_seen_all(match_info):
    '''
    How long since each matched person was seen on Tinder.

    :param match_info: value from calling :method: `get_match_info`.

    :return: `dict`.
    '''
    return { match_info[person]['name']: how_long_since_last_seen(person) for person in match_info }


def pause():
    '''
    In order to appear as a real Tinder user using the app...
    When making many API calls, it is important to pause a...
    realistic amount of time between actions to not make Tinder...
    suspicious!
    '''
    pause_duration = 3 * random()
    sleep(pause_duration)