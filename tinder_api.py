import json
from datetime import datetime

import requests
import tinder_config as config

headers = {
    'app_version': '6.9.4',
    'platform': 'ios',
    "content-type": "application/json",
    "User-agent": "Tinder/4.7.1 (iPhone; iOS 9.2; Scale/2.00)",
}

"""
Known endpoints:
	tested:
		-- https://api.gotinder.com/auth
		-- https://api.gotinder.com/user/recs
		-- https://api.gotinder.com/user/matches/_id
		-- https://api.gotinder.com/user/_id
		-- https://api.gotinder.com/updates
		-- https://api.gotinder.com/profile
		-- https://api.gotinder.com/meta
		-- https://api.gotinder.com/user/ping
		-- https://api.gotinder.com/report/{_id}
		-- https://api.gotinder.com/{like|pass}/{_id}
	untested:
		https://api.gotinder.com/group/{like|pass}/{id}
		https://api.gotinder.com/passport/user/travel
"""


""" TO DO :
1. Figure out sorting by date
2. Create thread to generate all matches info upon startup
3. Create master function? since all the functions are similar just with different
	endpoints and GET/POST
4. Look for error/test cases?
5. How can i use this ??
"""

def get_auth_token(fb_auth_token, fb_user_id):
	url = config.host + '/auth'
	req = requests.post(url,
    	headers=headers,
    	data=json.dumps({'facebook_token': fb_auth_token, 'facebook_id': fb_user_id})
    	)
	try:
		tinder_auth_token = req.json()["token"]
		headers.update({"X-Auth-Token": tinder_auth_token})
		return tinder_auth_token
	except:
		return {"error": "could not authorize"}

tinder_auth_token = get_auth_token(config.fb_auth_token, config.fb_user_id)

# INPUT : None
# OUTPUT: A dict of the recommended users to swipe on
# I think recommended means the users who have already 'liked' you
# r.json()["results"][index]["name"] == the person at index's name
def get_recommendations():
	try:
		r = requests.get('https://api.gotinder.com/user/recs', headers=headers)
		return r.json()
	except:
		return {"error": "could not retrieve recommendations"}

		##### COULD DO LIKE IF "ERROR" IN r.json() then print this else do this.


# INPUT: last_activity_date -> the date from which you want to see updates
#							-> defaults to "" which means from the beginning of time
# 		should be of the form ______________________
# OUTPUT: A dict of all updates since given activity date
# NOTES: You can do this to get messages sent, all matches...
def get_updates(last_activity_date=""):
	r = requests.post('https://api.gotinder.com/updates',
		headers=headers,
		data=json.dumps({"last_activity_date": last_activity_date}))
	return r.json()

# Returns the following keys:
## ['squads_only', 'squads_discoverable', 'instagram', 
## 'gender', 'bio', 'birth_date', 'name', 'interested_in', 
## 'location', 'gender_filter', 'age_filter_min', 'photos', 
## 'ping_time', 'squad_ads_shown', 'discoverable', 'facebook_id', 
## 'pos', 'can_create_squad', 'age_filter_max', 'schools', 
## 'pos_info', 'jobs', 'blend', 'distance_filter', '_id', 
## 'create_date']
def get_self():
	url = config.host + '/profile'
	r = requests.get(url, headers=headers)
	return r.json()


# 18 >= age_filter_min <= 46
# 22 >- age_filter_max <= 55
# age_filter_min <= age_filter_max - 4
# gender 0 = looking for males, gender 1 = looking for females
# 1 <= distance_filter >= 100 in miles
def change_preferences(age_filter_min, age_filter_max, gender, distance_filter):
	url = config.host + '/profile'
	preferences = {"age_filter_min": age_filter_min,
		 "gender": gender,
		 "age_filter_max": age_filter_max, 
		 "distance_filter": distance_filter}
	r = requests.post(url, headers=headers, data=json.dumps(preferences))
	return r.json()

# Returns metadata containing the following keys:
## ['globals', 'client_resources', 'versions', 'purchases', 
## 'status', 'groups', 'products', 'rating', 'tutorials', 
## 'travel', 'notifications', 'user']
def get_meta():
	url = config.host + '/meta'
	r = requests.get(url, headers=headers)
	return r.json()

def get_ping(lat, lon):
	headers.update({"X-Auth-Token": tinder_auth_token})
	url = config.host + '/user/ping'
	r = requests.post(url, headers=headers, data={"lat": lat, "lon": lon})
	return r.json()

# Input: person_id --> the tinder_id of a user not yourself
# Output: The person_id's corresponding profile information
#		bio, pictures, gender, birthdate...

# NEED A FUNCTION TO GET THAT PERSON'S ID FROM THE UPDATES CALL
def get_person(person_id):
	url = config.host + '/user/%s' % person_id
	r = requests.get(url, headers=headers)
	return r.json()

# INPUT: match_id : string -> 
#	this is different than the person's person_id
#	the match_id is typically an id for the chat
# 	usually, match_id = person1_id ^ person2_id
# 	get_updates["matches"][0]["_id"] is the match_id for match 0, the index
# INPUT: msg : string -> 
#	Desired message to be sent
# OUTPUT: Success or Failure msg
def send_msg(match_id, msg):
	url = config.host + '/user/matches/%s' % match_id
	r = requests.get(url, headers=headers, data=json.dumps({"message": msg}))
	return r.json()

def superlike(person_id):
	url = config.host + '/like/%s/super' % person_id
	r = requests.get(url, headers=headers)
	return r.json()	

def like(person_id):
	url = config.host + '/like/%s' % person_id
	r = requests.get(url, headers=headers)
	return r.json()

def dislike(person_id):
	url = config.host + '/pass/%s' % person_id
	r = requests.get(url, headers=headers)
	return r.json()

# Cause must be one of the given options
# I WILL CHECK THESE LATER
def report(person_id, cause):
	url = config.host + '/report/%s' % person_id
	r = requests.post(url, headers=headers, data={"cause": cause})
	return r.json()


################################################
################################################
################################################
################################################

# To sort by distance
# the call is get_person(id)['results']['distance_mi']

# To sort by time
# the call is get_updates()['matches'][INDEX]['person']['ping_time']

# To sort by total messages
# the call is get_updates()['matches'][INDEX]['message_count']

# To sort by gender:
# the call is get_updates()['matches'][0]['person']['gender']

# To get bio:
# the call is get_updates()['matches'][INDEX]['person']['bio']

# To get list of photos:
# the call is get_photos_by_person_id(person_id)

# To get person_id by name:
# the call is get_match_id_by_name

def get_match_info():
	matches = get_updates()['matches']
	name_dict = {}
	for match in matches:
		person = match['person']
		name = person['name']
		person_id = person['_id']
		match_id = match['id']
		ping_time = person['ping_time']
		birthday = person['birth_date'][:10]
		message_count = match['message_count']
		# photos = get_photos_by_person_id(person_id)
		bio = person['bio']
		gender = person['gender']
		# distance = get_person(person_id)['results']['distance_mi']
		name_dict[person_id] = {
			"name": name,
			"ping_time": ping_time,
			"match_id": match_id,
			"birthday": birthday,
			"message_count": message_count,
			# "photos": photos,
			"bio": bio,
			"gender": gender,
			# "distance": distance
		}
	return name_dict

def get_match_id_by_name(name):
	match_info = get_match_info()
	for match in match_info:
		match_name = match_info[match]['name']
		if match_name == name:
			return match_info[match]['match_id']
	return {"error": "No matches by name of %s" % name}

def get_photos_by_person_id(person_id):
	person = get_person(person_id)
	photo_urls = []
	for photo in person['results']['photos']:
		photo_urls.append(photo['url'])
	return photo_urls

# def sort_by_message_count():
# 	matches = get_match_info()
# 	msg_count = []
# 	for match in matches:
# 		msg_count.append(match['message_count'])

# Upon starting the program i should start a separate thread that basically begins get_matches
# so that all the data is stored locally after about a minute but behind the scenes.


# It is probably a good idea to 
# go through each match and create a dict from 
# name -> match_id 
# and then create another thing that will list each matches name






