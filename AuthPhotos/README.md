### Getting Facebook Token

The facebook_token is a little bit complicated as of now. First you must go <a href="https://www.facebook.com/v2.6/dialog/oauth?redirect_uri=fb464891386855067%3A%2F%2Fauthorize%2F&display=touch&state=%7B%22challenge%22%3A%22IUUkEUqIGud332lfu%252BMJhxL4Wlc%253D%22%2C%220_auth_logger_id%22%3A%2230F06532-A1B9-4B10-BB28-B29956C71AB1%22%2C%22com.facebook.sdk_client_state%22%3Atrue%2C%223_method%22%3A%22sfvc_auth%22%7D&scope=user_birthday%2Cuser_photos%2Cuser_education_history%2Cemail%2Cuser_relationship_details%2Cuser_friends%2Cuser_work_history%2Cuser_likes&response_type=token%2Csigned_request&default_audience=friends&return_scopes=true&auth_type=rerequest&client_id=464891386855067&ret=login&sdk=ios&logger_id=30F06532-A1B9-4B10-BB28-B29956C71AB1&ext=1470840777&hash=AeZqkIcf-NEW6vBd">here</a> to allow Tinder access to your Facebook. If you have a Tinder account, you probably have already done this. 

Before pressing the 'OK' button, open up the Developer Tools for your browser and navigate to the 'Network' section. Then press the 'OK' button. 

<img src='https://github.com/fbessez/Tinder/blob/master/AuthPhotos/auth1.png' alt='Auth1' style="width:128px;height:128px;"> 

This should cause the 'Network' section to show a 'name' beginning with 'confirm?dpr=2' as seen in the photo below. Click on this and also click on the 'Response' tab. This should look similar to how it does in the picture below. If you Command + F for 'access_token', it should lead you to a portion of the response that reads 'access_token=EJOFIJ...OAIEJI&expires'. Copy and paste everything from access_token= to the &. This is the facebook_token that you should place in your config file. This particular token will only last about an hour or two so just keep that in mind.

<img src='https://github.com/fbessez/Tinder/blob/master/AuthPhotos/auth2.png' alt='Auth2' style="width:128px;height:128px;"> 


### How to get facebook_id
This one is much simpler. Visit <a href='http://findmyfbid.com/'> this </a> website and it should be pretty simple. Simply paste in the url to your Facebook timeline and it should return your correct facebook_id. Copy and Paste this value into your config file. 