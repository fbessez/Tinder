import json
from datetime import datetime

import requests
import tinder_config as config

headers = {
    'app_version': '3',
    'platform': 'ios',
    "content-type": "application/json",
    "User-agent": "Tinder/4.7.1 (iPhone; iOS 9.2; Scale/2.00)",
}

"""
Known endpoints:

-- https://api.gotinder.com/user/recs
-- https://api.gotinder.com/user/matches/_id
-- https://api.gotinder.com/user/_id
-- https://api.gotinder.com/updates
-- https://api.gotinder.com/profile
-- https://api.gotinder.com/meta
https://api.gotinder.com/user/ping
-- https://api.gotinder.com/{like|pass}/{_id}
https://api.gotinder.com/group/{like|pass}/{id}
https://api.gotinder.com/passport/user/travel
https://api.gotinder.com/report/{_id}
"""

def get_auth_token(fb_auth_token, fb_user_id):
	url = config.host + '/auth'
	req = requests.post(url,
    	headers=headers,
    	data=json.dumps({'facebook_token': fb_auth_token, 'facebook_id': fb_user_id})
    	)
	try:
		return req.json()["token"]
		headers.update({"X-Auth-Token": tinder_auth_token})
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
	r = requests.post(url, headers=headers)
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




