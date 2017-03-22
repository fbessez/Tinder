from datetime import date, timedelta, datetime
from threading import Thread
import time
import tinder_api as api


################################################
################################################
################################################
################################################

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
	now = datetime.utcnow()
	match_info = {}
	for match in matches[:len(matches) - 2]:
		try:
			person = match['person']
			name = person['name']
			person_id = person['_id'] # for looking up profile
			match_id = match['id'] # for sending messages
			ping_time = person['ping_time']
			message_count = match['message_count']
			photos = get_photos(person)
			bio = person['bio']
			gender = person['gender']
			messages = match['messages']
			birthday = match['person']['birth_date']
			avg_successRate = get_avg_successRate(person)
			# distance = person_json['results']['distance_mi'] #Takes too long...

			match_info[person_id] = {
				"name": name,
				"ping_time": ping_time,
				"last_activity_date": get_last_activity_date(now, ping_time),
				"match_id": match_id,
				"message_count": message_count,
				"photos": photos,
				"bio": bio,
				"gender": gender,
				"avg_successRate": avg_successRate,
				"messages": messages,
				"age": calculate_age(birthday)
				# "distance": distance,
			}

		except Exception as ex:
		    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
		    message = template.format(type(ex).__name__, ex.args)
		    print(message)
	print("All data stored in match_info")
	return match_info

# Query the name 
def get_match_id_by_name(name):
	global match_info
	list_of_ids = []
	for match in match_info:
		match_name = match_info[match]['name']
		if match_name == name:
			list_of_ids += match_info[match]['match_id']
	if len(list_of_ids) > 0:
		return list_of_ids
	return {"error": "No matches by name of %s" % name}

# Returns a list of photo urls
def get_photos(person):
	photos = person['photos']
	photo_urls = []
	for photo in photos:
		photo_urls = photo_urls + [photo['url']]
	return photo_urls

# Converts from '1997-03-25T22:49:41.151Z' to an integer (age)
def calculate_age(birthday_string):
	birthyear = int(birthday_string[:4])
	birthmonth = int(birthday_string[5:7])
	birthday = int(birthday_string[8:10])
	today = date.today()
	return today.year - birthyear - ((today.month, today.day) < (birthmonth, birthday))

# Gets the average successRate of the person
# perhaps an indicator of... something? 
def get_avg_successRate(person):
	photos = person['photos']
	avg = 0
	for photo in photos:
		try:
			photo_successRate = photo['successRate']
			avg += photo_successRate
		except:
			return 0
	return avg / len(photos)

# From difference to readable string
def convert_from_datetime(difference):
	# datetime will be an input of datetime.timedelta(difference.days, difference.seconds, difference.microseconds)
	secs = difference.seconds
	days = difference.days
	m, s = divmod(secs, 60)
	h, m = divmod(m, 60)
	return ("%d days, %d hrs %02d min %02d sec" % (days, h, m, s))

# Convert from datetime class to string
# and then gets the difference from now til then
def get_last_activity_date(now, ping_time):
	ping_time = ping_time[:len(ping_time) - 5]
	datetime_ping = datetime.strptime(ping_time, '%Y-%m-%dT%H:%M:%S')
	difference = now - datetime_ping
	since = convert_from_datetime(difference)
	return since

# For sorting by last_activity
def how_long_has_it_been():
	global match_info
	now = datetime.utcnow()
	times = {}
	for person in match_info:
		name = match_info[person]['name']
		ping_time = match_info[person]['ping_time']
		since = get_last_activity_date(now, ping_time)
		times[name] = since
		print(name, "----->", since)
	return times

def sort_by_successRate():
	global match_info
	return sorted(match_info.items(), key=lambda x: x[1]['avg_successRate'], reverse=True)

def sort_by_activity_date():
	global match_info
	return sorted(match_info.items(), key=lambda x: x[1]['last_activity_date'])

# This is the abstract version of sort_by_activity_date and sort_by_successRate
# accepted valueNames are: "age", "last_activity_date", "message_count", "successRate", "gender"
def sort_by_value(valueName):
	global match_info
	return sorted(match_info.items(), key=lambda x: x[1][valueName], reverse=True)
# This doesn't sort it...Maybe make it a list?
# Can't return a sorted dict.

match_info = get_match_info()

### GLOBALS:
'''
match_info
			{
				"name": name, 
				"ping_time": ping_time,
				"last_activity_date": get_last_activity_date(now, ping_time),
				"match_id": match_id,
				"message_count": message_count,
				"photos": photos,
				"bio": bio,
				"gender": gender,
				"avg_successRate": avg_successRate,
				"messages": messages
				# "distance": distance,
			}
'''

##### Thread no longer necessary because
##### it runs very quickly...
# class MyThread(Thread):
# 	def __init__(self, val):
# 		Thread.__init__(self)
# 		self.val = val
# 	def run(self):
# 		global match_info
# 		match_info = get_match_info()
# 		print("All match info stored in local var: match_info")

# matchthread = MyThread(0)
# matchthread.start()
# print("Functions: how_long_has_it_been, get_photos_by_person_id, get_match_id_by_name")
# print("Gathering data on your matches...")
# while match_info == {}:
# 	print("...")
# 	time.sleep(2)



