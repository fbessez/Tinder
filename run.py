from datetime import date, timedelta, datetime
from threading import Thread
import tinder_api as api

### GLOBALS:
match_info = {}


### KNOWN BUGS:
# get_match_info fails when you have tinder social matches
# the fields change for those matches
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


THESE ARE THE NEW FIELDS
HAVE TO FILTER IF PERSON in get_match_info is an individual or a group!
{
  'owner': '588a824a73564ae27e84f8f8',
  'all_members': [
    {
      'birth_date': '1996-02-21T13:59:57.017Z',
      'gender': 0,
      'name': 'Aaron',
      'photos': [
        {
          'processedFiles': [
            {
              'url': 'http://images.gotinder.com/582bf32045abd633680f17f8/640x640_a829866d-2b4f-4e8a-af62-fec3116f1e31.jpg',
              'width': 640,
              'height': 640
            },
            {
              'url': 'http://images.gotinder.com/582bf32045abd633680f17f8/320x320_a829866d-2b4f-4e8a-af62-fec3116f1e31.jpg',
              'width': 320,
              'height': 320
            },
            {
              'url': 'http://images.gotinder.com/582bf32045abd633680f17f8/172x172_a829866d-2b4f-4e8a-af62-fec3116f1e31.jpg',
              'width': 172,
              'height': 172
            },
            {
              'url': 'http://images.gotinder.com/582bf32045abd633680f17f8/84x84_a829866d-2b4f-4e8a-af62-fec3116f1e31.jpg',
              'width': 84,
              'height': 84
            }
          ],
          'id': 'a829866d-2b4f-4e8a-af62-fec3116f1e31',
          'xoffset_percent': 0,
          'extension': 'jpg',
          'yoffset_percent': 0,
          'ydistance_percent': 1,
          'main': False,
          'fileName': 'a829866d-2b4f-4e8a-af62-fec3116f1e31.jpg',
          'selectRate': 0,
          'url': 'http://images.gotinder.com/582bf32045abd633680f17f8/a829866d-2b4f-4e8a-af62-fec3116f1e31.jpg',
          'successRate': 0.02531645569620253,
          'xdistance_percent': 1
        },
        {
          'processedFiles': [
            {
              'url': 'http://images.gotinder.com/582bf32045abd633680f17f8/640x640_3570106f-7c88-4d18-8550-c075935d376f.jpg',
              'width': 640,
              'height': 640
            },
            {
              'url': 'http://images.gotinder.com/582bf32045abd633680f17f8/320x320_3570106f-7c88-4d18-8550-c075935d376f.jpg',
              'width': 320,
              'height': 320
            },
            {
              'url': 'http://images.gotinder.com/582bf32045abd633680f17f8/172x172_3570106f-7c88-4d18-8550-c075935d376f.jpg',
              'width': 172,
              'height': 172
            },
            {
              'url': 'http://images.gotinder.com/582bf32045abd633680f17f8/84x84_3570106f-7c88-4d18-8550-c075935d376f.jpg',
              'width': 84,
              'height': 84
            }
          ],
          'id': '3570106f-7c88-4d18-8550-c075935d376f',
          'xoffset_percent': 0,
          'extension': 'jpg',
          'yoffset_percent': 0.1711873421087621,
          'ydistance_percent': 0.5905963302752293,
          'main': False,
          'fileName': '3570106f-7c88-4d18-8550-c075935d376f.jpg',
          'selectRate': 0,
          'url': 'http://images.gotinder.com/582bf32045abd633680f17f8/3570106f-7c88-4d18-8550-c075935d376f.jpg',
          'successRate': 0,
          'xdistance_percent': 1
        },
        {
          'processedFiles': [
            {
              'url': 'http://images.gotinder.com/582bf32045abd633680f17f8/640x640_acb3941e-f534-4f19-861b-62c40e9044b6.jpg',
              'width': 640,
              'height': 640
            },
            {
              'url': 'http://images.gotinder.com/582bf32045abd633680f17f8/320x320_acb3941e-f534-4f19-861b-62c40e9044b6.jpg',
              'width': 320,
              'height': 320
            },
            {
              'url': 'http://images.gotinder.com/582bf32045abd633680f17f8/172x172_acb3941e-f534-4f19-861b-62c40e9044b6.jpg',
              'width': 172,
              'height': 172
            },
            {
              'url': 'http://images.gotinder.com/582bf32045abd633680f17f8/84x84_acb3941e-f534-4f19-861b-62c40e9044b6.jpg',
              'width': 84,
              'height': 84
            }
          ],
          'id': 'acb3941e-f534-4f19-861b-62c40e9044b6',
          'xoffset_percent': 0,
          'extension': 'jpg',
          'yoffset_percent': 0,
          'ydistance_percent': 1,
          'main': False,
          'fileName': 'acb3941e-f534-4f19-861b-62c40e9044b6.jpg',
          'selectRate': 0,
          'url': 'http://images.gotinder.com/582bf32045abd633680f17f8/acb3941e-f534-4f19-861b-62c40e9044b6.jpg',
          'successRate': 0,
          'xdistance_percent': 0.6675938803894299
        },
        {
          'extension': 'jpg',
          'fileName': 'c7fa00ee-98b0-4899-8f68-4ef291c977d1.jpg',
          'main': 'main',
          'selectRate': 0,
          'processedFiles': [
            {
              'url': 'http://images.gotinder.com/582bf32045abd633680f17f8/640x640_c7fa00ee-98b0-4899-8f68-4ef291c977d1.jpg',
              'width': 640,
              'height': 640
            },
            {
              'url': 'http://images.gotinder.com/582bf32045abd633680f17f8/320x320_c7fa00ee-98b0-4899-8f68-4ef291c977d1.jpg',
              'width': 320,
              'height': 320
            },
            {
              'url': 'http://images.gotinder.com/582bf32045abd633680f17f8/172x172_c7fa00ee-98b0-4899-8f68-4ef291c977d1.jpg',
              'width': 172,
              'height': 172
            },
            {
              'url': 'http://images.gotinder.com/582bf32045abd633680f17f8/84x84_c7fa00ee-98b0-4899-8f68-4ef291c977d1.jpg',
              'width': 84,
              'height': 84
            }
          ],
          'id': 'c7fa00ee-98b0-4899-8f68-4ef291c977d1',
          'shape': 'center_square',
          'url': 'http://images.gotinder.com/582bf32045abd633680f17f8/c7fa00ee-98b0-4899-8f68-4ef291c977d1.jpg',
          'successRate': 0
        }
      ],
      'badges': [
        
      ],
      'bio': "Wesleyan '19\nI just need a friend to eat Chipotle with.",
      '_id': '582bf32045abd633680f17f8',
      'ping_time': '2017-02-18T04:57:31.239Z'
    },
    {
      'birth_date': '1995-02-21T13:59:57.021Z',
      'gender': 1,
      'name': 'Fabien',
      'photos': [
        {
          'ydistance_percent': 0.9888639559785721,
          'processedFiles': [
            {
              'width': 640,
              'url': 'http://images.gotinder.com/588a824a73564ae27e84f8f8/640x640_737a16a3-b0ed-4f10-8861-4f8ce530ac33.jpg',
              'height': 640
            },
            {
              'width': 320,
              'url': 'http://images.gotinder.com/588a824a73564ae27e84f8f8/320x320_737a16a3-b0ed-4f10-8861-4f8ce530ac33.jpg',
              'height': 320
            },
            {
              'width': 172,
              'url': 'http://images.gotinder.com/588a824a73564ae27e84f8f8/172x172_737a16a3-b0ed-4f10-8861-4f8ce530ac33.jpg',
              'height': 172
            },
            {
              'width': 84,
              'url': 'http://images.gotinder.com/588a824a73564ae27e84f8f8/84x84_737a16a3-b0ed-4f10-8861-4f8ce530ac33.jpg',
              'height': 84
            }
          ],
          'xoffset_percent': 0.249819500079447,
          'main': False,
          'id': '737a16a3-b0ed-4f10-8861-4f8ce530ac33',
          'fileName': '737a16a3-b0ed-4f10-8861-4f8ce530ac33.jpg',
          'extension': 'jpg',
          'url': 'http://images.gotinder.com/588a824a73564ae27e84f8f8/737a16a3-b0ed-4f10-8861-4f8ce530ac33.jpg',
          'yoffset_percent': 0.02470851135174154,
          'xdistance_percent': 0.6578692151579667
        },
        {
          'processedFiles': [
            {
              'width': 640,
              'url': 'http://images.gotinder.com/588a824a73564ae27e84f8f8/640x640_c45f1967-a013-4e91-8595-0be6ff517e6b.jpg',
              'height': 640
            },
            {
              'width': 320,
              'url': 'http://images.gotinder.com/588a824a73564ae27e84f8f8/320x320_c45f1967-a013-4e91-8595-0be6ff517e6b.jpg',
              'height': 320
            },
            {
              'width': 172,
              'url': 'http://images.gotinder.com/588a824a73564ae27e84f8f8/172x172_c45f1967-a013-4e91-8595-0be6ff517e6b.jpg',
              'height': 172
            },
            {
              'width': 84,
              'url': 'http://images.gotinder.com/588a824a73564ae27e84f8f8/84x84_c45f1967-a013-4e91-8595-0be6ff517e6b.jpg',
              'height': 84
            }
          ],
          'main': 'main',
          'extension': 'jpg',
          'fileName': 'c45f1967-a013-4e91-8595-0be6ff517e6b.jpg',
          'shape': 'center_square',
          'url': 'http://images.gotinder.com/588a824a73564ae27e84f8f8/c45f1967-a013-4e91-8595-0be6ff517e6b.jpg',
          'id': 'c45f1967-a013-4e91-8595-0be6ff517e6b'
        },
        {
          'processedFiles': [
            {
              'width': 640,
              'url': 'http://images.gotinder.com/588a824a73564ae27e84f8f8/640x640_b6d3a39a-62d9-4b71-a5d8-3b1fc43a3e84.jpg',
              'height': 640
            },
            {
              'width': 320,
              'url': 'http://images.gotinder.com/588a824a73564ae27e84f8f8/320x320_b6d3a39a-62d9-4b71-a5d8-3b1fc43a3e84.jpg',
              'height': 320
            },
            {
              'width': 172,
              'url': 'http://images.gotinder.com/588a824a73564ae27e84f8f8/172x172_b6d3a39a-62d9-4b71-a5d8-3b1fc43a3e84.jpg',
              'height': 172
            },
            {
              'width': 84,
              'url': 'http://images.gotinder.com/588a824a73564ae27e84f8f8/84x84_b6d3a39a-62d9-4b71-a5d8-3b1fc43a3e84.jpg',
              'height': 84
            }
          ],
          'extension': 'jpg',
          'fileName': 'b6d3a39a-62d9-4b71-a5d8-3b1fc43a3e84.jpg',
          'shape': 'center_square',
          'url': 'http://images.gotinder.com/588a824a73564ae27e84f8f8/b6d3a39a-62d9-4b71-a5d8-3b1fc43a3e84.jpg',
          'id': 'b6d3a39a-62d9-4b71-a5d8-3b1fc43a3e84'
        },
        {
          'ydistance_percent': 0.4202479139224885,
          'xoffset_percent': 0.3288231536617898,
          'fileName': '59896fa2-d5e6-4506-8bf5-1982475b46e8.jpg',
          'main': False,
          'processedFiles': [
            {
              'url': 'http://images.gotinder.com/588a824a73564ae27e84f8f8/640x640_59896fa2-d5e6-4506-8bf5-1982475b46e8.jpg',
              'width': 640,
              'height': 640
            },
            {
              'url': 'http://images.gotinder.com/588a824a73564ae27e84f8f8/320x320_59896fa2-d5e6-4506-8bf5-1982475b46e8.jpg',
              'width': 320,
              'height': 320
            },
            {
              'url': 'http://images.gotinder.com/588a824a73564ae27e84f8f8/172x172_59896fa2-d5e6-4506-8bf5-1982475b46e8.jpg',
              'width': 172,
              'height': 172
            },
            {
              'url': 'http://images.gotinder.com/588a824a73564ae27e84f8f8/84x84_59896fa2-d5e6-4506-8bf5-1982475b46e8.jpg',
              'width': 84,
              'height': 84
            }
          ],
          'id': '59896fa2-d5e6-4506-8bf5-1982475b46e8',
          'extension': 'jpg',
          'url': 'http://images.gotinder.com/588a824a73564ae27e84f8f8/59896fa2-d5e6-4506-8bf5-1982475b46e8.jpg',
          'yoffset_percent': 0.3227801733272113,
          'xdistance_percent': 0.5603305518966514
        },
        {
          'id': 'db443bf2-fb0a-45c9-bb28-a0840ecf6e30',
          'processedFiles': [
            {
              'url': 'http://images.gotinder.com/588a824a73564ae27e84f8f8/640x640_db443bf2-fb0a-45c9-bb28-a0840ecf6e30.jpg',
              'width': 640,
              'height': 640
            },
            {
              'url': 'http://images.gotinder.com/588a824a73564ae27e84f8f8/320x320_db443bf2-fb0a-45c9-bb28-a0840ecf6e30.jpg',
              'width': 320,
              'height': 320
            },
            {
              'url': 'http://images.gotinder.com/588a824a73564ae27e84f8f8/172x172_db443bf2-fb0a-45c9-bb28-a0840ecf6e30.jpg',
              'width': 172,
              'height': 172
            },
            {
              'url': 'http://images.gotinder.com/588a824a73564ae27e84f8f8/84x84_db443bf2-fb0a-45c9-bb28-a0840ecf6e30.jpg',
              'width': 84,
              'height': 84
            }
          ],
          'fileName': 'db443bf2-fb0a-45c9-bb28-a0840ecf6e30.jpg',
          'extension': 'jpg',
          'url': 'http://images.gotinder.com/588a824a73564ae27e84f8f8/db443bf2-fb0a-45c9-bb28-a0840ecf6e30.jpg'
        }
      ],
      'bio': 'Searching for my waifu 🇫🇷 🇨🇱 \n"Clear eyes, full hearts, can\'t lose" - Michael Scott',
      '_id': '588a824a73564ae27e84f8f8',
      'ping_time': '2017-02-18T13:53:03.787Z'
    }
  ],
  'my_group': [
    '582bf32045abd633680f17f8',
    '588a824a73564ae27e84f8f8'
  ],
  'update_time': '2017-02-17T14:06:19.790Z',
  'expired': False,
  'muted': False,
  'closed': False,
  'created_date': '2017-02-17T14:06:19.790Z',
  'id': 'J6jXLaqVzL',
  'my_group_id': 'J6jXLaqVzL'
}
'''
'''
THIS IS NA EXAMPLE OF A DIFFERENT MATCH 

{
  'is_super_like': False,
  'id': 'Yo39kvfKXaG3',
  'created_date': '2017-02-18T04:45:01.292Z',
  'muted': False,
  'expired': False,
  'all_members': [
    {
      '_id': '582bf32045abd633680f17f8',
      'badges': [
        
      ],
      'name': 'Aaron',
      'bio': "Wesleyan '19\nI just need a friend to eat Chipotle with.",
      'gender': 0,
      'ping_time': '2017-02-18T04:57:31.239Z',
      'photos': [
        {
          'main': False,
          'id': 'a829866d-2b4f-4e8a-af62-fec3116f1e31',
          'yoffset_percent': 0,
          'successRate': 0.02531645569620253,
          'xoffset_percent': 0,
          'extension': 'jpg',
          'xdistance_percent': 1,
          'url': 'http://images.gotinder.com/582bf32045abd633680f17f8/a829866d-2b4f-4e8a-af62-fec3116f1e31.jpg',
          'ydistance_percent': 1,
          'selectRate': 0,
          'processedFiles': [
            {
              'width': 640,
              'height': 640,
              'url': 'http://images.gotinder.com/582bf32045abd633680f17f8/640x640_a829866d-2b4f-4e8a-af62-fec3116f1e31.jpg'
            },
            {
              'width': 320,
              'height': 320,
              'url': 'http://images.gotinder.com/582bf32045abd633680f17f8/320x320_a829866d-2b4f-4e8a-af62-fec3116f1e31.jpg'
            },
            {
              'width': 172,
              'height': 172,
              'url': 'http://images.gotinder.com/582bf32045abd633680f17f8/172x172_a829866d-2b4f-4e8a-af62-fec3116f1e31.jpg'
            },
            {
              'width': 84,
              'height': 84,
              'url': 'http://images.gotinder.com/582bf32045abd633680f17f8/84x84_a829866d-2b4f-4e8a-af62-fec3116f1e31.jpg'
            }
          ],
          'fileName': 'a829866d-2b4f-4e8a-af62-fec3116f1e31.jpg'
        },
        {
          'main': False,
          'id': '3570106f-7c88-4d18-8550-c075935d376f',
          'yoffset_percent': 0.1711873421087621,
          'successRate': 0,
          'xoffset_percent': 0,
          'extension': 'jpg',
          'xdistance_percent': 1,
          'url': 'http://images.gotinder.com/582bf32045abd633680f17f8/3570106f-7c88-4d18-8550-c075935d376f.jpg',
          'ydistance_percent': 0.5905963302752293,
          'selectRate': 0,
          'processedFiles': [
            {
              'width': 640,
              'height': 640,
              'url': 'http://images.gotinder.com/582bf32045abd633680f17f8/640x640_3570106f-7c88-4d18-8550-c075935d376f.jpg'
            },
            {
              'width': 320,
              'height': 320,
              'url': 'http://images.gotinder.com/582bf32045abd633680f17f8/320x320_3570106f-7c88-4d18-8550-c075935d376f.jpg'
            },
            {
              'width': 172,
              'height': 172,
              'url': 'http://images.gotinder.com/582bf32045abd633680f17f8/172x172_3570106f-7c88-4d18-8550-c075935d376f.jpg'
            },
            {
              'width': 84,
              'height': 84,
              'url': 'http://images.gotinder.com/582bf32045abd633680f17f8/84x84_3570106f-7c88-4d18-8550-c075935d376f.jpg'
            }
          ],
          'fileName': '3570106f-7c88-4d18-8550-c075935d376f.jpg'
        },
        {
          'main': False,
          'id': 'acb3941e-f534-4f19-861b-62c40e9044b6',
          'yoffset_percent': 0,
          'successRate': 0,
          'xoffset_percent': 0,
          'extension': 'jpg',
          'xdistance_percent': 0.6675938803894299,
          'url': 'http://images.gotinder.com/582bf32045abd633680f17f8/acb3941e-f534-4f19-861b-62c40e9044b6.jpg',
          'ydistance_percent': 1,
          'selectRate': 0,
          'processedFiles': [
            {
              'width': 640,
              'height': 640,
              'url': 'http://images.gotinder.com/582bf32045abd633680f17f8/640x640_acb3941e-f534-4f19-861b-62c40e9044b6.jpg'
            },
            {
              'width': 320,
              'height': 320,
              'url': 'http://images.gotinder.com/582bf32045abd633680f17f8/320x320_acb3941e-f534-4f19-861b-62c40e9044b6.jpg'
            },
            {
              'width': 172,
              'height': 172,
              'url': 'http://images.gotinder.com/582bf32045abd633680f17f8/172x172_acb3941e-f534-4f19-861b-62c40e9044b6.jpg'
            },
            {
              'width': 84,
              'height': 84,
              'url': 'http://images.gotinder.com/582bf32045abd633680f17f8/84x84_acb3941e-f534-4f19-861b-62c40e9044b6.jpg'
            }
          ],
          'fileName': 'acb3941e-f534-4f19-861b-62c40e9044b6.jpg'
        },
        {
          'successRate': 0,
          'main': 'main',
          'selectRate': 0,
          'id': 'c7fa00ee-98b0-4899-8f68-4ef291c977d1',
          'extension': 'jpg',
          'url': 'http://images.gotinder.com/582bf32045abd633680f17f8/c7fa00ee-98b0-4899-8f68-4ef291c977d1.jpg',
          'shape': 'center_square',
          'processedFiles': [
            {
              'width': 640,
              'height': 640,
              'url': 'http://images.gotinder.com/582bf32045abd633680f17f8/640x640_c7fa00ee-98b0-4899-8f68-4ef291c977d1.jpg'
            },
            {
              'width': 320,
              'height': 320,
              'url': 'http://images.gotinder.com/582bf32045abd633680f17f8/320x320_c7fa00ee-98b0-4899-8f68-4ef291c977d1.jpg'
            },
            {
              'width': 172,
              'height': 172,
              'url': 'http://images.gotinder.com/582bf32045abd633680f17f8/172x172_c7fa00ee-98b0-4899-8f68-4ef291c977d1.jpg'
            },
            {
              'width': 84,
              'height': 84,
              'url': 'http://images.gotinder.com/582bf32045abd633680f17f8/84x84_c7fa00ee-98b0-4899-8f68-4ef291c977d1.jpg'
            }
          ],
          'fileName': 'c7fa00ee-98b0-4899-8f68-4ef291c977d1.jpg'
        }
      ],
      'birth_date': '1996-02-21T14:03:31.209Z'
    },
    {
      '_id': '587572a31b13942943f707e5',
      'badges': [
        
      ],
      'name': 'Adam',
      'bio': "Music and Computer Science major, Wesleyan '17\n\n<something ironic goes here>",
      'gender': 0,
      'ping_time': '2017-02-17T14:17:29.842Z',
      'photos': [
        {
          'successRate': 0.10526315789473684,
          'main': 'main',
          'shape': 'center_square',
          'id': 'c9fea09e-29d3-44a5-a7ac-8c9ae2416011',
          'extension': 'jpg',
          'url': 'http://images.gotinder.com/587572a31b13942943f707e5/c9fea09e-29d3-44a5-a7ac-8c9ae2416011.jpg',
          'selectRate': 0,
          'processedFiles': [
            {
              'url': 'http://images.gotinder.com/587572a31b13942943f707e5/640x640_c9fea09e-29d3-44a5-a7ac-8c9ae2416011.jpg',
              'height': 640,
              'width': 640
            },
            {
              'url': 'http://images.gotinder.com/587572a31b13942943f707e5/320x320_c9fea09e-29d3-44a5-a7ac-8c9ae2416011.jpg',
              'height': 320,
              'width': 320
            },
            {
              'url': 'http://images.gotinder.com/587572a31b13942943f707e5/172x172_c9fea09e-29d3-44a5-a7ac-8c9ae2416011.jpg',
              'height': 172,
              'width': 172
            },
            {
              'url': 'http://images.gotinder.com/587572a31b13942943f707e5/84x84_c9fea09e-29d3-44a5-a7ac-8c9ae2416011.jpg',
              'height': 84,
              'width': 84
            }
          ],
          'fileName': 'c9fea09e-29d3-44a5-a7ac-8c9ae2416011.jpg'
        },
        {
          'url': 'http://images.gotinder.com/587572a31b13942943f707e5/04996aa9-2266-4f61-83bc-723996d4217d.jpg',
          'fileName': '04996aa9-2266-4f61-83bc-723996d4217d.jpg',
          'processedFiles': [
            {
              'url': 'http://images.gotinder.com/587572a31b13942943f707e5/640x640_04996aa9-2266-4f61-83bc-723996d4217d.jpg',
              'height': 640,
              'width': 640
            },
            {
              'url': 'http://images.gotinder.com/587572a31b13942943f707e5/320x320_04996aa9-2266-4f61-83bc-723996d4217d.jpg',
              'height': 320,
              'width': 320
            },
            {
              'url': 'http://images.gotinder.com/587572a31b13942943f707e5/172x172_04996aa9-2266-4f61-83bc-723996d4217d.jpg',
              'height': 172,
              'width': 172
            },
            {
              'url': 'http://images.gotinder.com/587572a31b13942943f707e5/84x84_04996aa9-2266-4f61-83bc-723996d4217d.jpg',
              'height': 84,
              'width': 84
            }
          ],
          'id': '04996aa9-2266-4f61-83bc-723996d4217d',
          'extension': 'jpg'
        },
        {
          'url': 'http://images.gotinder.com/587572a31b13942943f707e5/06634c17-2025-4c4b-8794-9e24f5a80f57.jpg',
          'fileName': '06634c17-2025-4c4b-8794-9e24f5a80f57.jpg',
          'processedFiles': [
            {
              'url': 'http://images.gotinder.com/587572a31b13942943f707e5/640x640_06634c17-2025-4c4b-8794-9e24f5a80f57.jpg',
              'height': 640,
              'width': 640
            },
            {
              'url': 'http://images.gotinder.com/587572a31b13942943f707e5/320x320_06634c17-2025-4c4b-8794-9e24f5a80f57.jpg',
              'height': 320,
              'width': 320
            },
            {
              'url': 'http://images.gotinder.com/587572a31b13942943f707e5/172x172_06634c17-2025-4c4b-8794-9e24f5a80f57.jpg',
              'height': 172,
              'width': 172
            },
            {
              'url': 'http://images.gotinder.com/587572a31b13942943f707e5/84x84_06634c17-2025-4c4b-8794-9e24f5a80f57.jpg',
              'height': 84,
              'width': 84
            }
          ],
          'id': '06634c17-2025-4c4b-8794-9e24f5a80f57',
          'extension': 'jpg'
        },
        {
          'successRate': 0.125,
          'id': '17f4601c-37b1-4db1-87d1-7082f05c72b5',
          'extension': 'jpg',
          'url': 'http://images.gotinder.com/587572a31b13942943f707e5/17f4601c-37b1-4db1-87d1-7082f05c72b5.jpg',
          'selectRate': 0,
          'processedFiles': [
            {
              'url': 'http://images.gotinder.com/587572a31b13942943f707e5/640x640_17f4601c-37b1-4db1-87d1-7082f05c72b5.jpg',
              'height': 640,
              'width': 640
            },
            {
              'url': 'http://images.gotinder.com/587572a31b13942943f707e5/320x320_17f4601c-37b1-4db1-87d1-7082f05c72b5.jpg',
              'height': 320,
              'width': 320
            },
            {
              'url': 'http://images.gotinder.com/587572a31b13942943f707e5/172x172_17f4601c-37b1-4db1-87d1-7082f05c72b5.jpg',
              'height': 172,
              'width': 172
            },
            {
              'url': 'http://images.gotinder.com/587572a31b13942943f707e5/84x84_17f4601c-37b1-4db1-87d1-7082f05c72b5.jpg',
              'height': 84,
              'width': 84
            }
          ],
          'fileName': '17f4601c-37b1-4db1-87d1-7082f05c72b5.jpg'
        },
        {
          'successRate': 0.0625,
          'id': '812f01f4-bdf4-4de5-8cd9-557ff0ca6d9c',
          'extension': 'jpg',
          'url': 'http://images.gotinder.com/587572a31b13942943f707e5/812f01f4-bdf4-4de5-8cd9-557ff0ca6d9c.jpg',
          'selectRate': 0,
          'processedFiles': [
            {
              'url': 'http://images.gotinder.com/587572a31b13942943f707e5/640x640_812f01f4-bdf4-4de5-8cd9-557ff0ca6d9c.jpg',
              'height': 640,
              'width': 640
            },
            {
              'url': 'http://images.gotinder.com/587572a31b13942943f707e5/320x320_812f01f4-bdf4-4de5-8cd9-557ff0ca6d9c.jpg',
              'height': 320,
              'width': 320
            },
            {
              'url': 'http://images.gotinder.com/587572a31b13942943f707e5/172x172_812f01f4-bdf4-4de5-8cd9-557ff0ca6d9c.jpg',
              'height': 172,
              'width': 172
            },
            {
              'url': 'http://images.gotinder.com/587572a31b13942943f707e5/84x84_812f01f4-bdf4-4de5-8cd9-557ff0ca6d9c.jpg',
              'height': 84,
              'width': 84
            }
          ],
          'fileName': '812f01f4-bdf4-4de5-8cd9-557ff0ca6d9c.jpg'
        }
      ],
      'birth_date': '1994-02-21T14:03:31.215Z'
    },
    {
      '_id': '588a824a73564ae27e84f8f8',
      'name': 'Fabien',
      'bio': 'Searching for my waifu 🇫🇷 🇨🇱 \n"Clear eyes, full hearts, can\'t lose" - Michael Scott',
      'gender': 1,
      'ping_time': '2017-02-18T13:53:03.787Z',
      'photos': [
        {
          'main': False,
          'xoffset_percent': 0.249819500079447,
          'ydistance_percent': 0.9888639559785721,
          'yoffset_percent': 0.02470851135174154,
          'extension': 'jpg',
          'xdistance_percent': 0.6578692151579667,
          'url': 'http://images.gotinder.com/588a824a73564ae27e84f8f8/737a16a3-b0ed-4f10-8861-4f8ce530ac33.jpg',
          'id': '737a16a3-b0ed-4f10-8861-4f8ce530ac33',
          'processedFiles': [
            {
              'url': 'http://images.gotinder.com/588a824a73564ae27e84f8f8/640x640_737a16a3-b0ed-4f10-8861-4f8ce530ac33.jpg',
              'height': 640,
              'width': 640
            },
            {
              'url': 'http://images.gotinder.com/588a824a73564ae27e84f8f8/320x320_737a16a3-b0ed-4f10-8861-4f8ce530ac33.jpg',
              'height': 320,
              'width': 320
            },
            {
              'url': 'http://images.gotinder.com/588a824a73564ae27e84f8f8/172x172_737a16a3-b0ed-4f10-8861-4f8ce530ac33.jpg',
              'height': 172,
              'width': 172
            },
            {
              'url': 'http://images.gotinder.com/588a824a73564ae27e84f8f8/84x84_737a16a3-b0ed-4f10-8861-4f8ce530ac33.jpg',
              'height': 84,
              'width': 84
            }
          ],
          'fileName': '737a16a3-b0ed-4f10-8861-4f8ce530ac33.jpg'
        },
        {
          'main': 'main',
          'id': 'c45f1967-a013-4e91-8595-0be6ff517e6b',
          'extension': 'jpg',
          'url': 'http://images.gotinder.com/588a824a73564ae27e84f8f8/c45f1967-a013-4e91-8595-0be6ff517e6b.jpg',
          'shape': 'center_square',
          'processedFiles': [
            {
              'url': 'http://images.gotinder.com/588a824a73564ae27e84f8f8/640x640_c45f1967-a013-4e91-8595-0be6ff517e6b.jpg',
              'height': 640,
              'width': 640
            },
            {
              'url': 'http://images.gotinder.com/588a824a73564ae27e84f8f8/320x320_c45f1967-a013-4e91-8595-0be6ff517e6b.jpg',
              'height': 320,
              'width': 320
            },
            {
              'url': 'http://images.gotinder.com/588a824a73564ae27e84f8f8/172x172_c45f1967-a013-4e91-8595-0be6ff517e6b.jpg',
              'height': 172,
              'width': 172
            },
            {
              'url': 'http://images.gotinder.com/588a824a73564ae27e84f8f8/84x84_c45f1967-a013-4e91-8595-0be6ff517e6b.jpg',
              'height': 84,
              'width': 84
            }
          ],
          'fileName': 'c45f1967-a013-4e91-8595-0be6ff517e6b.jpg'
        },
        {
          'id': 'b6d3a39a-62d9-4b71-a5d8-3b1fc43a3e84',
          'extension': 'jpg',
          'url': 'http://images.gotinder.com/588a824a73564ae27e84f8f8/b6d3a39a-62d9-4b71-a5d8-3b1fc43a3e84.jpg',
          'shape': 'center_square',
          'processedFiles': [
            {
              'url': 'http://images.gotinder.com/588a824a73564ae27e84f8f8/640x640_b6d3a39a-62d9-4b71-a5d8-3b1fc43a3e84.jpg',
              'height': 640,
              'width': 640
            },
            {
              'url': 'http://images.gotinder.com/588a824a73564ae27e84f8f8/320x320_b6d3a39a-62d9-4b71-a5d8-3b1fc43a3e84.jpg',
              'height': 320,
              'width': 320
            },
            {
              'url': 'http://images.gotinder.com/588a824a73564ae27e84f8f8/172x172_b6d3a39a-62d9-4b71-a5d8-3b1fc43a3e84.jpg',
              'height': 172,
              'width': 172
            },
            {
              'url': 'http://images.gotinder.com/588a824a73564ae27e84f8f8/84x84_b6d3a39a-62d9-4b71-a5d8-3b1fc43a3e84.jpg',
              'height': 84,
              'width': 84
            }
          ],
          'fileName': 'b6d3a39a-62d9-4b71-a5d8-3b1fc43a3e84.jpg'
        },
        {
          'main': False,
          'xoffset_percent': 0.3288231536617898,
          'id': '59896fa2-d5e6-4506-8bf5-1982475b46e8',
          'yoffset_percent': 0.3227801733272113,
          'extension': 'jpg',
          'xdistance_percent': 0.5603305518966514,
          'url': 'http://images.gotinder.com/588a824a73564ae27e84f8f8/59896fa2-d5e6-4506-8bf5-1982475b46e8.jpg',
          'fileName': '59896fa2-d5e6-4506-8bf5-1982475b46e8.jpg',
          'processedFiles': [
            {
              'width': 640,
              'height': 640,
              'url': 'http://images.gotinder.com/588a824a73564ae27e84f8f8/640x640_59896fa2-d5e6-4506-8bf5-1982475b46e8.jpg'
            },
            {
              'width': 320,
              'height': 320,
              'url': 'http://images.gotinder.com/588a824a73564ae27e84f8f8/320x320_59896fa2-d5e6-4506-8bf5-1982475b46e8.jpg'
            },
            {
              'width': 172,
              'height': 172,
              'url': 'http://images.gotinder.com/588a824a73564ae27e84f8f8/172x172_59896fa2-d5e6-4506-8bf5-1982475b46e8.jpg'
            },
            {
              'width': 84,
              'height': 84,
              'url': 'http://images.gotinder.com/588a824a73564ae27e84f8f8/84x84_59896fa2-d5e6-4506-8bf5-1982475b46e8.jpg'
            }
          ],
          'ydistance_percent': 0.4202479139224885
        },
        {
          'url': 'http://images.gotinder.com/588a824a73564ae27e84f8f8/db443bf2-fb0a-45c9-bb28-a0840ecf6e30.jpg',
          'extension': 'jpg',
          'processedFiles': [
            {
              'width': 640,
              'height': 640,
              'url': 'http://images.gotinder.com/588a824a73564ae27e84f8f8/640x640_db443bf2-fb0a-45c9-bb28-a0840ecf6e30.jpg'
            },
            {
              'width': 320,
              'height': 320,
              'url': 'http://images.gotinder.com/588a824a73564ae27e84f8f8/320x320_db443bf2-fb0a-45c9-bb28-a0840ecf6e30.jpg'
            },
            {
              'width': 172,
              'height': 172,
              'url': 'http://images.gotinder.com/588a824a73564ae27e84f8f8/172x172_db443bf2-fb0a-45c9-bb28-a0840ecf6e30.jpg'
            },
            {
              'width': 84,
              'height': 84,
              'url': 'http://images.gotinder.com/588a824a73564ae27e84f8f8/84x84_db443bf2-fb0a-45c9-bb28-a0840ecf6e30.jpg'
            }
          ],
          'id': 'db443bf2-fb0a-45c9-bb28-a0840ecf6e30',
          'fileName': 'db443bf2-fb0a-45c9-bb28-a0840ecf6e30.jpg'
        }
      ],
      'birth_date': '1995-02-21T14:03:31.216Z'
    },
    {
      '_id': '58a78481393f21507e87dd5d',
      'name': 'Chris',
      'bio': '🚱',
      'gender': 0,
      'ping_time': '2017-02-18T00:34:54.791Z',
      'photos': [
        {
          'main': 'main',
          'id': '596123db-a42d-4dd8-b19b-241d737a4191',
          'extension': 'jpg',
          'url': 'http://images.gotinder.com/58a78481393f21507e87dd5d/596123db-a42d-4dd8-b19b-241d737a4191.jpg',
          'shape': 'center_square',
          'processedFiles': [
            {
              'width': 640,
              'height': 640,
              'url': 'http://images.gotinder.com/58a78481393f21507e87dd5d/640x640_596123db-a42d-4dd8-b19b-241d737a4191.jpg'
            },
            {
              'width': 320,
              'height': 320,
              'url': 'http://images.gotinder.com/58a78481393f21507e87dd5d/320x320_596123db-a42d-4dd8-b19b-241d737a4191.jpg'
            },
            {
              'width': 172,
              'height': 172,
              'url': 'http://images.gotinder.com/58a78481393f21507e87dd5d/172x172_596123db-a42d-4dd8-b19b-241d737a4191.jpg'
            },
            {
              'width': 84,
              'height': 84,
              'url': 'http://images.gotinder.com/58a78481393f21507e87dd5d/84x84_596123db-a42d-4dd8-b19b-241d737a4191.jpg'
            }
          ],
          'fileName': '596123db-a42d-4dd8-b19b-241d737a4191.jpg'
        },
        {
          'main': False,
          'xoffset_percent': 0,
          'ydistance_percent': 1,
          'yoffset_percent': 0,
          'extension': 'jpg',
          'xdistance_percent': 1,
          'url': 'http://images.gotinder.com/58a78481393f21507e87dd5d/067acec2-1775-4d45-8914-a22eb793ba52.jpg',
          'id': '067acec2-1775-4d45-8914-a22eb793ba52',
          'processedFiles': [
            {
              'url': 'http://images.gotinder.com/58a78481393f21507e87dd5d/640x640_067acec2-1775-4d45-8914-a22eb793ba52.jpg',
              'height': 640,
              'width': 640
            },
            {
              'url': 'http://images.gotinder.com/58a78481393f21507e87dd5d/320x320_067acec2-1775-4d45-8914-a22eb793ba52.jpg',
              'height': 320,
              'width': 320
            },
            {
              'url': 'http://images.gotinder.com/58a78481393f21507e87dd5d/172x172_067acec2-1775-4d45-8914-a22eb793ba52.jpg',
              'height': 172,
              'width': 172
            },
            {
              'url': 'http://images.gotinder.com/58a78481393f21507e87dd5d/84x84_067acec2-1775-4d45-8914-a22eb793ba52.jpg',
              'height': 84,
              'width': 84
            }
          ],
          'fileName': '067acec2-1775-4d45-8914-a22eb793ba52.jpg'
        },
        {
          'url': 'http://images.gotinder.com/58a78481393f21507e87dd5d/a866a5a8-2bb4-458f-8bf6-af2e227324dd.jpg',
          'extension': 'jpg',
          'processedFiles': [
            {
              'width': 640,
              'height': 640,
              'url': 'http://images.gotinder.com/58a78481393f21507e87dd5d/640x640_a866a5a8-2bb4-458f-8bf6-af2e227324dd.jpg'
            },
            {
              'width': 320,
              'height': 320,
              'url': 'http://images.gotinder.com/58a78481393f21507e87dd5d/320x320_a866a5a8-2bb4-458f-8bf6-af2e227324dd.jpg'
            },
            {
              'width': 172,
              'height': 172,
              'url': 'http://images.gotinder.com/58a78481393f21507e87dd5d/172x172_a866a5a8-2bb4-458f-8bf6-af2e227324dd.jpg'
            },
            {
              'width': 84,
              'height': 84,
              'url': 'http://images.gotinder.com/58a78481393f21507e87dd5d/84x84_a866a5a8-2bb4-458f-8bf6-af2e227324dd.jpg'
            }
          ],
          'id': 'a866a5a8-2bb4-458f-8bf6-af2e227324dd',
          'fileName': 'a866a5a8-2bb4-458f-8bf6-af2e227324dd.jpg'
        },
        {
          'url': 'http://images.gotinder.com/58a78481393f21507e87dd5d/dfcb3de2-bdd0-4722-bf4f-a8348414959b.jpg',
          'extension': 'jpg',
          'processedFiles': [
            {
              'width': 640,
              'height': 640,
              'url': 'http://images.gotinder.com/58a78481393f21507e87dd5d/640x640_dfcb3de2-bdd0-4722-bf4f-a8348414959b.jpg'
            },
            {
              'width': 320,
              'height': 320,
              'url': 'http://images.gotinder.com/58a78481393f21507e87dd5d/320x320_dfcb3de2-bdd0-4722-bf4f-a8348414959b.jpg'
            },
            {
              'width': 172,
              'height': 172,
              'url': 'http://images.gotinder.com/58a78481393f21507e87dd5d/172x172_dfcb3de2-bdd0-4722-bf4f-a8348414959b.jpg'
            },
            {
              'width': 84,
              'height': 84,
              'url': 'http://images.gotinder.com/58a78481393f21507e87dd5d/84x84_dfcb3de2-bdd0-4722-bf4f-a8348414959b.jpg'
            }
          ],
          'id': 'dfcb3de2-bdd0-4722-bf4f-a8348414959b',
          'fileName': 'dfcb3de2-bdd0-4722-bf4f-a8348414959b.jpg'
        },
        {
          'url': 'http://images.gotinder.com/58a78481393f21507e87dd5d/1ba290c4-7af9-4b6a-8103-4fdb25f5ea38.jpg',
          'fileName': '1ba290c4-7af9-4b6a-8103-4fdb25f5ea38.jpg',
          'processedFiles': [
            {
              'url': 'http://images.gotinder.com/58a78481393f21507e87dd5d/640x640_1ba290c4-7af9-4b6a-8103-4fdb25f5ea38.jpg',
              'height': 640,
              'width': 640
            },
            {
              'url': 'http://images.gotinder.com/58a78481393f21507e87dd5d/320x320_1ba290c4-7af9-4b6a-8103-4fdb25f5ea38.jpg',
              'height': 320,
              'width': 320
            },
            {
              'url': 'http://images.gotinder.com/58a78481393f21507e87dd5d/172x172_1ba290c4-7af9-4b6a-8103-4fdb25f5ea38.jpg',
              'height': 172,
              'width': 172
            },
            {
              'url': 'http://images.gotinder.com/58a78481393f21507e87dd5d/84x84_1ba290c4-7af9-4b6a-8103-4fdb25f5ea38.jpg',
              'height': 84,
              'width': 84
            }
          ],
          'id': '1ba290c4-7af9-4b6a-8103-4fdb25f5ea38',
          'extension': 'jpg'
        },
        {
          'main': False,
          'xoffset_percent': 0,
          'ydistance_percent': 0.5625,
          'yoffset_percent': 0.219,
          'extension': 'jpg',
          'xdistance_percent': 0.9999999999999999,
          'url': 'http://images.gotinder.com/58a78481393f21507e87dd5d/ccb2baf6-cc2a-41c8-92e5-6b7b40f77a26.jpg',
          'id': 'ccb2baf6-cc2a-41c8-92e5-6b7b40f77a26',
          'processedFiles': [
            {
              'url': 'http://images.gotinder.com/58a78481393f21507e87dd5d/640x640_ccb2baf6-cc2a-41c8-92e5-6b7b40f77a26.jpg',
              'height': 640,
              'width': 640
            },
            {
              'url': 'http://images.gotinder.com/58a78481393f21507e87dd5d/320x320_ccb2baf6-cc2a-41c8-92e5-6b7b40f77a26.jpg',
              'height': 320,
              'width': 320
            },
            {
              'url': 'http://images.gotinder.com/58a78481393f21507e87dd5d/172x172_ccb2baf6-cc2a-41c8-92e5-6b7b40f77a26.jpg',
              'height': 172,
              'width': 172
            },
            {
              'url': 'http://images.gotinder.com/58a78481393f21507e87dd5d/84x84_ccb2baf6-cc2a-41c8-92e5-6b7b40f77a26.jpg',
              'height': 84,
              'width': 84
            }
          ],
          'fileName': 'ccb2baf6-cc2a-41c8-92e5-6b7b40f77a26.jpg'
        }
      ],
      'birth_date': '1994-02-21T14:03:31.218Z'
    },
    {
      '_id': '58a7a2c01f6d4c9234eaddd6',
      'name': 'Torie',
      'bio': '',
      'gender': 1,
      'ping_time': '2017-02-18T01:26:23.018Z',
      'photos': [
        {
          'url': 'http://images.gotinder.com/58a7a2c01f6d4c9234eaddd6/51f4db0f-e2f1-47bf-841b-b32ae371e6e7.jpg',
          'extension': 'jpg',
          'processedFiles': [
            {
              'width': 640,
              'height': 640,
              'url': 'http://images.gotinder.com/58a7a2c01f6d4c9234eaddd6/640x640_51f4db0f-e2f1-47bf-841b-b32ae371e6e7.jpg'
            },
            {
              'width': 320,
              'height': 320,
              'url': 'http://images.gotinder.com/58a7a2c01f6d4c9234eaddd6/320x320_51f4db0f-e2f1-47bf-841b-b32ae371e6e7.jpg'
            },
            {
              'width': 172,
              'height': 172,
              'url': 'http://images.gotinder.com/58a7a2c01f6d4c9234eaddd6/172x172_51f4db0f-e2f1-47bf-841b-b32ae371e6e7.jpg'
            },
            {
              'width': 84,
              'height': 84,
              'url': 'http://images.gotinder.com/58a7a2c01f6d4c9234eaddd6/84x84_51f4db0f-e2f1-47bf-841b-b32ae371e6e7.jpg'
            }
          ],
          'id': '51f4db0f-e2f1-47bf-841b-b32ae371e6e7',
          'fileName': '51f4db0f-e2f1-47bf-841b-b32ae371e6e7.jpg'
        },
        {
          'url': 'http://images.gotinder.com/58a7a2c01f6d4c9234eaddd6/992114f9-a7ae-4a00-89a3-e16f2a5703e3.jpg',
          'extension': 'jpg',
          'processedFiles': [
            {
              'width': 640,
              'height': 640,
              'url': 'http://images.gotinder.com/58a7a2c01f6d4c9234eaddd6/640x640_992114f9-a7ae-4a00-89a3-e16f2a5703e3.jpg'
            },
            {
              'width': 320,
              'height': 320,
              'url': 'http://images.gotinder.com/58a7a2c01f6d4c9234eaddd6/320x320_992114f9-a7ae-4a00-89a3-e16f2a5703e3.jpg'
            },
            {
              'width': 172,
              'height': 172,
              'url': 'http://images.gotinder.com/58a7a2c01f6d4c9234eaddd6/172x172_992114f9-a7ae-4a00-89a3-e16f2a5703e3.jpg'
            },
            {
              'width': 84,
              'height': 84,
              'url': 'http://images.gotinder.com/58a7a2c01f6d4c9234eaddd6/84x84_992114f9-a7ae-4a00-89a3-e16f2a5703e3.jpg'
            }
          ],
          'id': '992114f9-a7ae-4a00-89a3-e16f2a5703e3',
          'fileName': '992114f9-a7ae-4a00-89a3-e16f2a5703e3.jpg'
        },
        {
          'url': 'http://images.gotinder.com/58a7a2c01f6d4c9234eaddd6/47840822-24d2-4ddb-8f37-ce98304af2eb.jpg',
          'fileName': '47840822-24d2-4ddb-8f37-ce98304af2eb.jpg',
          'processedFiles': [
            {
              'url': 'http://images.gotinder.com/58a7a2c01f6d4c9234eaddd6/640x640_47840822-24d2-4ddb-8f37-ce98304af2eb.jpg',
              'height': 640,
              'width': 640
            },
            {
              'url': 'http://images.gotinder.com/58a7a2c01f6d4c9234eaddd6/320x320_47840822-24d2-4ddb-8f37-ce98304af2eb.jpg',
              'height': 320,
              'width': 320
            },
            {
              'url': 'http://images.gotinder.com/58a7a2c01f6d4c9234eaddd6/172x172_47840822-24d2-4ddb-8f37-ce98304af2eb.jpg',
              'height': 172,
              'width': 172
            },
            {
              'url': 'http://images.gotinder.com/58a7a2c01f6d4c9234eaddd6/84x84_47840822-24d2-4ddb-8f37-ce98304af2eb.jpg',
              'height': 84,
              'width': 84
            }
          ],
          'id': '47840822-24d2-4ddb-8f37-ce98304af2eb',
          'extension': 'jpg'
        },
        {
          'url': 'http://images.gotinder.com/58a7a2c01f6d4c9234eaddd6/3c9369f7-0f99-4ec0-8fc4-38ddc190a1a1.jpg',
          'extension': 'jpg',
          'processedFiles': [
            {
              'width': 640,
              'height': 640,
              'url': 'http://images.gotinder.com/58a7a2c01f6d4c9234eaddd6/640x640_3c9369f7-0f99-4ec0-8fc4-38ddc190a1a1.jpg'
            },
            {
              'width': 320,
              'height': 320,
              'url': 'http://images.gotinder.com/58a7a2c01f6d4c9234eaddd6/320x320_3c9369f7-0f99-4ec0-8fc4-38ddc190a1a1.jpg'
            },
            {
              'width': 172,
              'height': 172,
              'url': 'http://images.gotinder.com/58a7a2c01f6d4c9234eaddd6/172x172_3c9369f7-0f99-4ec0-8fc4-38ddc190a1a1.jpg'
            },
            {
              'width': 84,
              'height': 84,
              'url': 'http://images.gotinder.com/58a7a2c01f6d4c9234eaddd6/84x84_3c9369f7-0f99-4ec0-8fc4-38ddc190a1a1.jpg'
            }
          ],
          'id': '3c9369f7-0f99-4ec0-8fc4-38ddc190a1a1',
          'fileName': '3c9369f7-0f99-4ec0-8fc4-38ddc190a1a1.jpg'
        },
        {
          'url': 'http://images.gotinder.com/58a7a2c01f6d4c9234eaddd6/900296e6-256a-418b-806f-81d0b0f83278.jpg',
          'fileName': '900296e6-256a-418b-806f-81d0b0f83278.jpg',
          'processedFiles': [
            {
              'url': 'http://images.gotinder.com/58a7a2c01f6d4c9234eaddd6/640x640_900296e6-256a-418b-806f-81d0b0f83278.jpg',
              'height': 640,
              'width': 640
            },
            {
              'url': 'http://images.gotinder.com/58a7a2c01f6d4c9234eaddd6/320x320_900296e6-256a-418b-806f-81d0b0f83278.jpg',
              'height': 320,
              'width': 320
            },
            {
              'url': 'http://images.gotinder.com/58a7a2c01f6d4c9234eaddd6/172x172_900296e6-256a-418b-806f-81d0b0f83278.jpg',
              'height': 172,
              'width': 172
            },
            {
              'url': 'http://images.gotinder.com/58a7a2c01f6d4c9234eaddd6/84x84_900296e6-256a-418b-806f-81d0b0f83278.jpg',
              'height': 84,
              'width': 84
            }
          ],
          'id': '900296e6-256a-418b-806f-81d0b0f83278',
          'extension': 'jpg'
        },
        {
          'url': 'http://images.gotinder.com/58a7a2c01f6d4c9234eaddd6/d91c47d9-06e9-49d7-8f16-2268aa744adf.jpg',
          'extension': 'jpg',
          'processedFiles': [
            {
              'width': 640,
              'height': 640,
              'url': 'http://images.gotinder.com/58a7a2c01f6d4c9234eaddd6/640x640_d91c47d9-06e9-49d7-8f16-2268aa744adf.jpg'
            },
            {
              'width': 320,
              'height': 320,
              'url': 'http://images.gotinder.com/58a7a2c01f6d4c9234eaddd6/320x320_d91c47d9-06e9-49d7-8f16-2268aa744adf.jpg'
            },
            {
              'width': 172,
              'height': 172,
              'url': 'http://images.gotinder.com/58a7a2c01f6d4c9234eaddd6/172x172_d91c47d9-06e9-49d7-8f16-2268aa744adf.jpg'
            },
            {
              'width': 84,
              'height': 84,
              'url': 'http://images.gotinder.com/58a7a2c01f6d4c9234eaddd6/84x84_d91c47d9-06e9-49d7-8f16-2268aa744adf.jpg'
            }
          ],
          'id': 'd91c47d9-06e9-49d7-8f16-2268aa744adf',
          'fileName': 'd91c47d9-06e9-49d7-8f16-2268aa744adf.jpg'
        }
      ],
      'birth_date': '1995-02-21T14:03:31.218Z'
    }
  ],
  'my_group': [
    '582bf32045abd633680f17f8',
    '588a824a73564ae27e84f8f8'
  ],
  'messages': [
    {
      '_id': '58a7d320498c68c9535c6542',
      'timestamp': 1487393568505,
      'created_date': '2017-02-18T04:52:48.505Z',
      'message': 'Fab!!!!!!!!!!!!!!!!!!!!! ❤',
      'from': '58a7a2c01f6d4c9234eaddd6',
      'match_id': 'Yo39kvfKXaG3',
      'sent_date': '2017-02-18T04:52:48.505Z',
      'to': '588a824a73564ae27e84f8f8'
    },
    {
      '_id': '58a7d3c6498c68c9535c75cd',
      'timestamp': 1487393734476,
      'created_date': '2017-02-18T04:55:34.476Z',
      'message': 'hi Torie <3 and friends',
      'from': '588a824a73564ae27e84f8f8',
      'match_id': 'Yo39kvfKXaG3',
      'sent_date': '2017-02-18T04:55:34.476Z',
      'to': '588a824a73564ae27e84f8f8'
    }
  ],
  'update_time': '2017-02-18T04:45:01.292Z',
  'their_group': [
    '587572a31b13942943f707e5',
    '58a78481393f21507e87dd5d',
    '58a7a2c01f6d4c9234eaddd6'
  ],
  'owner': '588a824a73564ae27e84f8f8',
  'their_group_id': 'DEwYGVKNry',
  'last_activity_date': '2017-02-18T04:55:34.476Z',
  'closed': False,
  'my_group_id': 'J6jXLaqVzL'
}
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
	matches = api.get_updates()['matches']
	now = datetime.utcnow()
	for match in matches[:len(matches) - 1]:
		name = match['person']['name']
		ping_time = match['person']['ping_time']
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
# matchthread.join()

# Upon starting the program i should start a separate thread that basically begins get_matches
# so that all the data is stored locally after about a minute but behind the scenes.


# It is probably a good idea to 
# go through each match and create a dict from 
# name -> match_id 
# and then create another thing that will list each matches name


