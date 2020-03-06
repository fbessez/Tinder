from tinder_api_sms import *
import urllib.request
import os


recs = get_recommendations()['results']


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

