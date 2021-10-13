from tinder.v3.auth.sms import SMSUser
from tinder.v2.auth.facebook import FBUSer

if __name__ == '__main__':
    # v3 SMS authentication
    user = SMSUser('phone', email='email')
    user.login()
    user.like_all()

    # v2 FB authentication
    user = FBUSer('fb email', 'fb password')
    user.login()
    user.like_all()