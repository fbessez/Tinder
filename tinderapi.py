from tinder_api_sms import *
import urllib.request
import os
from time import sleep
import datetime


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
            distance_km = girl['distance_mi'] * 1.609
            i += 1
            like(girl['_id'])
            print('{} liked {}'.format(i, girl['name']))
            print('School: {} '.format(girl['schools']))
            print('{} km'.format(distance_km))
            print('------------------------------------------')
            # get second match list
            for user in matches:
                person = user['person']
                matched_ids.append(user['id'])
                secondmatch = len(matched_ids)
            # check if second list are longer than first list
            if  secondmatch - firstmatch == 1:
                print("It's a Match: {}".format(girl['name']))
                matched_ids.append(girl['_id'])
            sleep(2)
            

def fetch_image(times):
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
        if i > times:
            break
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
        matchage= int(person['birth_date'][:4]) - int(str(datetime.date.today())[:4])
        print('age: {} ({}) '.format(matchage, person['birth_date'][:4]))
        print('__________________________________________')
        
        