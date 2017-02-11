'''
the url to get your fb_auth_token:
https://www.facebook.com/v2.6/dialog/oauth?redirect_uri=fb464891386855067%3A%2F%2Fauthorize%2F&display=touch&state=%7B%22challenge%22%3A%22IUUkEUqIGud332lfu%252BMJhxL4Wlc%253D%22%2C%220_auth_logger_id%22%3A%2230F06532-A1B9-4B10-BB28-B29956C71AB1%22%2C%22com.facebook.sdk_client_state%22%3Atrue%2C%223_method%22%3A%22sfvc_auth%22%7D&scope=user_birthday%2Cuser_photos%2Cuser_education_history%2Cemail%2Cuser_relationship_details%2Cuser_friends%2Cuser_work_history%2Cuser_likes&response_type=token%2Csigned_request&default_audience=friends&return_scopes=true&auth_type=rerequest&client_id=464891386855067&ret=login&sdk=ios&logger_id=30F06532-A1B9-4B10-BB28-B29956C71AB1&ext=1470840777&hash=AeZqkIcf-NEW6vBd
When you go to this url, you will be asked to allow tinder access to your facebook
Presumably, this has already been done. Before pressing 'ok',
Open up the Developer Tools in Chrome by going View -> Developer -> Developer Tools
Here, you will see a series of tabs, one of which will be 'Networks'
Click on this.
On the Name sidebar there should be one that begins with 'confirm?dpr='
Click on that.
Now there should be a tab that says "Response" inside of which will begin
with: for (;;); {"..."}. In this response, there will be a part that says
"access_token=<access_token>&expires"
Copy and Paste that <access_token> below where <fb_token> is written

I am working on getting this fb_token programmatically
 
** This technique gets a token that only lasts for a short (1hour) period of time **

the url to get your fb_user_id:
http://findmyfbid.com/
'''

fb_auth_token = <fb_token>
fb_user_id = <id>