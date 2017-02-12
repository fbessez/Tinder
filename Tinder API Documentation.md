Tinder API Documentation -- 2017

First off, I want to give a shoutout to @rtt who initially posted the Tinder API Documentation that I found most of these endpoints on

**Note: This was written in February 2017. API might be outdated.**

### API Details 
<table>
	<tbody>
		<tr>
			<td>Host</td>
			<td>api.gotinder.com</td>
		</tr>
		<tr>
			<td>Protocol</td>
			<td>SSL</td>
		</tr>
	</tbody>
</table>

### Required Headers
<table>
	<thead>
		<tr>
			<th>Header</th>
			<th>Example</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>X-Auth-Token</td>
			<td>insert explanation</td>
		</tr>
		<tr>
			<td>Content-type</td>
			<td>application/json</td>
		</tr>
		<tr>
			<td>User-agent</td>
			<td>Tinder/4.7.1 (iPhone; iOS 9.2; Scale/2.00)</td>
		</tr>
	</tbody>
</table>

### Known Endpoints
Note: All endpoints are concatenated to the host api
Note: All curls must be sent with the headers as well (the only exception is that the /auth call must not have the X-Auth-Token header)
<table>
	<thead>
		<tr>
			<th>Endpoint</th>
			<th>Purpose</th>
			<th>Data?</th>
			<th>Get/Post/Delete</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>/auth</td>
			<td>For authenticating</td>
			<td>{'facebook_token': INSERT_HERE, 'facebook_id': INSERT_HERE}</td>
			<td>POST</td>
		</tr>
		<tr>
			<td>/user/recs</td>
			<td>Get match recommendations</td>
			<td>{}</td>
			<td>GET</td>
		</tr>
		<tr>
			<td>/user/matches/_id</td>
			<td>Send Message to that id</td>
			<td>{"message": TEXT GOES HERE}</td>
			<td>GET</td>
		</tr>
		<tr>
			<td>/user/_id</td>
			<td>Get a user's profile data</td>
			<td>{}</td>
			<td>GET</td>
		</tr>
		<tr>
			<td>/user/ping</td>
			<td>Change your location</td>
			<td>{"lat": lat, "lon": lon}</td>
			<td>POST</td>
		</tr>
		<tr>
			<td>/updates</td>
			<td>Get all updates since the given date -- inserting "" will give you all updates since creating a Tinder account (i.e. matches, messages sent, etc.)</td>
			<td>{"last_activity_date": ""}</td>
			<td>POST</td>
		</tr>
		<tr>
			<td>/profile</td>
			<td>Get your own profile data</td>
			<td>{}</td>
			<td>GET</td>
		</tr>
		<tr>
			<td>/profile</td>
			<td>Change your search preferences</td>
			<td>{"age_filter_min": age_filter_min,
				"gender": gender,
				"age_filter_max": age_filter_max, 
				"distance_filter": distance_filter}</td>
			<td>POST</td>
		</tr>
		<tr>
			<td>/meta</td>
			<td>Get your own meta data (swipes left, people seen, etc..)</td>
			<td>{}</td>
			<td>GET</td>
		</tr>
		<tr>
			<td>/report/_id</td>
			<td>Report someone --> There are only a few accepted causes...</td>
			<td>{"cause": CAUSE}</td>
			<td>POST</td>
		</tr>
		<tr>
			<td>/like/_id</td>
			<td>Like someone a.k.a swipe right</td>
			<td>{}</td>
			<td>GET</td>
		</tr>
		<tr>
			<td>/pass/_id</td>
			<td>Pass on someone a.k.a swipe left</td>
			<td>{}</td>
			<td>GET</td>
		</tr>
		<tr>
			<td>/like/_id/super</td>
			<td>~Super Like~ someone a.k.a swipe up</td>
			<td>{}</td>
			<td>GET</td>
		</tr>
		<tr>
			<td>/group/{like|pass}/_id</td>
			<td>Like or Pass on a group</td>
			<td>{}</td>
			<td>GET</td>
		</tr>
	</tbody>
</table>

### How to get facebook_token
The facebook_token is a little bit complicated as of now. First you must go <a href="https://www.facebook.com/v2.6/dialog/oauth?redirect_uri=fb464891386855067%3A%2F%2Fauthorize%2F&display=touch&state=%7B%22challenge%22%3A%22IUUkEUqIGud332lfu%252BMJhxL4Wlc%253D%22%2C%220_auth_logger_id%22%3A%2230F06532-A1B9-4B10-BB28-B29956C71AB1%22%2C%22com.facebook.sdk_client_state%22%3Atrue%2C%223_method%22%3A%22sfvc_auth%22%7D&scope=user_birthday%2Cuser_photos%2Cuser_education_history%2Cemail%2Cuser_relationship_details%2Cuser_friends%2Cuser_work_history%2Cuser_likes&response_type=token%2Csigned_request&default_audience=friends&return_scopes=true&auth_type=rerequest&client_id=464891386855067&ret=login&sdk=ios&logger_id=30F06532-A1B9-4B10-BB28-B29956C71AB1&ext=1470840777&hash=AeZqkIcf-NEW6vBd">here</a> to allow Tinder access to your Facebook. If you have a Tinder account, you probably have already done this. 

Before pressing the 'OK' button, open up the Developer Tools for your browser and navigate to the 'Network' section. Then press the 'OK' button. 

<img src='https://github.com/fbessez/Tinder/blob/master/AuthPhotos/auth1.png' alt='Auth1' style="width:128px;height:128px;"> 

This should cause the 'Network' section to show a 'name' beginning with 'confirm?dpr=2' as seen in the photo below. Click on this and also click on the 'Response' tab. This should look similar to how it does in the picture below. If you Command + F for 'access_token', it should lead you to a portion of the response that reads 'access_token=EJOFIJ...OAIEJI&expires'. Copy and paste everything from access_token= to the &. This is the facebook_token that you should place in your config file. 

<img src='https://github.com/fbessez/Tinder/blob/master/AuthPhotos/auth2.png' alt='Auth2' style="width:128px;height:128px;"> 

### How to get facebook_id
This one is much simpler. Visit <a href='http://findmyfbid.com/'> this </a> website and it should be pretty simple. Simply paste in the url to your Facebook timeline and it should return your correct facebook_id. Copy and Paste this value into your config file as well. 


























