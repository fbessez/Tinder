from tinder_api_sms import *
import urllib.request
import os
from time import sleep


recs = get_recommendations()['results']

def auto_like():
    matched_ids = []
    firstmatch = len(matched_ids)
    i = 0
    count = 70
    matches_dict = all_matches('{}'.format(count))
    matches = matches_dict['data']['matches']
    # get first match list
    for user in matches:
        person = user['person']
        matched_ids.append(user['id'])
        
    while True:
        # like girl in recommendations
        for girl in recs:
            i += 1
            like(girl['_id'])
            print('{} liked {}'.format(i, girl['name']))
            # get second match list
            for user in matches:
                person = user['person']
                if person['id'] not in matched_ids:
                    matched_ids.append(person['id'])
                    secondmatch = len(matched_ids)
            # check if second list are longer than first list
            if  firstmatch < secondmatch:
                print("It's a Match: {}".format(girl['name']))
                matched_ids.append(girl['_id'])
            sleep(3)

def fetch_image():
    print('fetching image...')
    i = 0
    # get each recommend in recs
    for person in recs:
        foldercount = 0
        i += 1
        print('___________{}___________'.format(i))
        print(person['name'])
        # get highlight photo of recommended's person
        for photo in person['photos']:
            try:
                os.mkdir("images/{}".format(person['name']))
            except FileExistsError:
                pass
            fullfilename = os.path.join("images/{}".format(person['name']), '{}.jpg'.format(foldercount))
            # download photo
            urllib.request.urlretrieve(photo['url'], fullfilename)
            print('downloaded: {} {}.jpg'.format(person['name'], foldercount))
            foldercount += 1
        print(' ')
        

def get_match_id():   
    i = 0
    count = 70
    matches_dict = all_matches('{}'.format(count))
    matches = matches_dict['data']['matches']
    for user in matches:
        person = user['person']
        i += 1
        print(i,user['id'] , person['name'])
        print(user['last_activity_date'])
        
        
def get_token():
    try:
        r = requests.get('https://api.gotinder.com/ws/generate?locale=en', headers=headers)
        return r.json()
    except requests.exceptions.RequestException as e:
        print("Something went wrong with getting recomendations:", e)

