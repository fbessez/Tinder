# coding=utf-8

import config
import tinder_api as api
import features

opener_message = 'Hey, did you read my bio'

def main():
    print("running main")
    print("likes remaining: {0}".format(features.get_likes_remaining()))
#    str = unicode('\x80abc', errors='replace')
#    print(str.encode('utf-8'))
#    like_all_nonad_recs()

def like_all_nonad_recs():
    get_recs = api.get_recs_v2()
    data = get_recs['data']
    if 'results' not in data:
        print(get_recs)
    recs = data['results']
    for rec in recs[:len(recs)]:
        user = rec['user']
        bio = user['bio']
        name = user['name'].encode('utf-8')
        id = user['_id']
        print(u'name: {0}, id: {1}'.format(name, id))
        if 'is_brand' in user and user['is_brand']:
            print(u'\tis_brand, will left-swipe now {0}'.format(api.dislike_and_pause(id)))
        else:
            like_response = features.like_and_pause(id)
            print(u'\tliking... {0}'.format(like_response))
            if like_response['match']:
                print('It\'s a match!')
                print(api.send_msg(id, opener_message))
            else:
                print('Aww, it\'s not a match:(')


if __name__ == '__main__':
    if api.authverif() == True:
        #print("Gathering Data on your matches...")
        #features.get_match_info()
        main()
    else:
        print("Something went wrong. You were not authorized.")

