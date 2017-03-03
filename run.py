from datetime import date, timedelta, datetime
from threading import Thread
import tinder_api as api

### GLOBALS:
match_info = {}

'''
Currently, I do not support anything for groups!

>>> b.keys() when b = my_group
dict_keys(['my_group', 'closed', 'owner', 'update_time', 
  'expired', 'muted', 'all_members', 'my_group_id', 'created_date', 'id'])

>>> c = x[40]
>>> c.keys() when c = other group
dict_keys(['closed', 'owner', 'messages', 'expired', 'their_group', 
  'all_members', 'created_date', 'my_group_id', 'is_super_like', 'last_activity_date', 
  'their_group_id', 'id', 'my_group', 'update_time', 'muted'])

>>> a.keys() when a = normal match
dict_keys(['closed', 'pending', 'message_count', 'is_boost_match', 
  'dead', 'participants', 'messages', 'person', 'created_date', 
  'common_like_count', 'common_friend_count', 'is_super_like', 
  'last_activity_date', 'following', '_id', 'id', 'following_moments'])

'''

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
	matches = api.get_updates()['matches']
	name_dict = {}
	for match in matches[:len(matches) - 2]:
		try:
			PERSON = match['person']
			name = PERSON['name']
			person_id = PERSON['_id'] # for looking up profile
			match_id = match['id'] # for sending messages
			person_json = api.get_person(person_id)
			ping_time = PERSON['ping_time']
			message_count = match['message_count']
			photos = get_photos_by_person_id(person_json)
			bio = PERSON['bio']
			gender = PERSON['gender']
			distance = person_json['results']['distance_mi']
			name_dict[person_id] = {
			"name": name,
			"ping_time": ping_time,
			"match_id": match_id,
			"message_count": message_count,
			"photos": photos,
			"bio": bio,
			"gender": gender,
			"distance": distance
			}
		except:
			continue
	return name_dict

def get_match_id_by_name(name):
	global match_info
	for match in match_info:
		match_name = match_info[match]['name']
		if match_name == name:
			return match_info[match]['match_id']
	return {"error": "No matches by name of %s" % name}

def get_photos_by_person_id(person_json):
	photo_urls = []
	for photo in person_json['results']['photos']:
		photo_urls.append(photo['url'])
	return photo_urls

def convert_from_datetime(difference):
	# datetime will be an input of datetime.timedelta(difference.days, difference.seconds, difference.microseconds)
	secs = difference.seconds
	days = difference.days
	m, s = divmod(secs, 60)
	h, m = divmod(m, 60)
	return ("%d days, %d hrs %02d min %02d sec" % (days, h, m, s))

def how_long_has_it_been():
  global match_info
  now = datetime.utcnow()
  for person in match_info:
    name = match_info[person]['name']
    ping_time = match_info[person]['ping_time']
    ping_time = ping_time[:len(ping_time) - 5]
    datetime_ping = datetime.strptime(ping_time, '%Y-%m-%dT%H:%M:%S')
    difference = now - datetime_ping
    since = convert_from_datetime(difference)
    print(name, "-->", since)

class MyThread(Thread):
	def __init__(self, val):
		Thread.__init__(self)
		self.val = val
	def run(self):
		global match_info
		match_info = get_match_info()
		print("All match info stored in local var: match_info")

matchthread = MyThread(0)
matchthread.start()



