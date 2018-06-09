# Tinder API Documentation - 2018

First off, I want to give a shoutout to <a href='https://gist.github.com/rtt/10403467#file-tinder-api-documentation-md'>@rtt</a> who initially posted the Tinder API Documentation that I found most of these endpoints on. I am writing this to provide a more up-to-date resource for working with the Tinder API.

**Note: This was updated in June 2018 so it might be outdated.**

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
			<td>See "How to get facebook_token" below</td>
		</tr>
		<tr>
			<td>Content-type</td>
			<td>application/json</td>
		</tr>
		<tr>
			<td>User-agent</td>
			<td>Tinder/7.5.3 (iPhone; iOS 10.3.2; Scale/2.00)</td>
		</tr>
	</tbody>
</table>

### Known Endpoints
Note: All endpoints are concatenated to the host url

Note: All curls must be sent with the headers as well (the only exception is that the /auth call must not have the X-Auth-Token header)
<table>
   <thead>
      <tr>
         <th>Endpoint</th>
         <th>Purpose</th>
         <th>Data?</th>
         <th>Method</th>
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
		 <td>/auth/login/accountkit</td>
		 <td>For SMS authentication (two-factor)</td>
		 <td>{'token': INSERT_HERE, 'id': INSERT_HERE, 'client_version':'9.0.1'}</td>
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
         <td>POST</td>
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
         <td>{"last_activity_date": ""} Input a timestamp: '2017-03-25T20:58:00.404Z' for updates since that time.</td>
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
         <td>{"age_filter_min": age_filter_min, "gender_filter": gender_filter, "gender": gender, "age_filter_max": age_filter_max, "distance_filter": distance_filter}</td>
         <td>POST</td>
      </tr>
      <tr>
         <td>/profile</td>
         <td>(Tinder Plus Only) hide/show age</td>
         <td>{"hide_age":boolean}</td>
         <td>POST</td>
      </tr>
      <tr>
         <td>/profile</td>
         <td>(Tinder Plus Only) hide/show distance</td>
         <td>{"hide_distance":boolean}</td>
         <td>POST</td>
      </tr>
      <tr>
         <td>/profile</td>
         <td>(Tinder Plus Only) hide/show ads</td>
         <td>{"hide_ads":boolean}</td>
         <td>POST</td>
      </tr>
      <tr>
         <td>/profile</td>
         <td>(Tinder Plus Only) Set Tinder Blend options to "Recent Activity": Shows more recently active users</td>
         <td>{"blend":"recency"}</td>
         <td>POST</td>
      </tr>
      <tr>
         <td>/profile</td>
         <td>(Tinder Plus Only) Set Tinder Blend options to "Optimal": Scientifically proven to get you more matches</td>
         <td>{"blend":"optimal"}</td>
         <td>POST</td>
      </tr>
      <tr>
         <td>/profile</td>
         <td>(Tinder Plus Only) Set discovery settings to only people who already liked you</td>
         <td>{"discoverable_party":"liked"}</td>
         <td>POST</td>
      </tr>
      <tr>
         <td>/passport/user/travel</td>
         <td>(Tinder Plus Only) Travel to coordinate</td>
         <td>{"lat":lat,"lon":lon}</td>
         <td>POST</td>
      </tr>
      <tr>
         <td>/instagram/authorize</td>
         <td>Auth Instagram</td>
         <td>{}</td>
         <td>GET</td>
      </tr>
      <tr>
         <td>/v2/profile/spotify/</td>
         <td>Get Spotify settings</td>
         <td>{}</td>
         <td>GET</td>
      </tr>
      <tr>
         <td>/v2/profile/spotify/theme</td>
         <td>Set Spotify song</td>
         <td>{"id":song_id}</td>
         <td>PUT</td>
      </tr>
      <tr>
         <td>/profile/username</td>
         <td>Change your webprofile username</td>
         <td>{"username": username}</td>
         <td>PUT</td>
      </tr>
      <tr>
         <td>/profile/username</td>
         <td>Reset your webprofile username</td>
         <td>{}</td>
         <td>DELETE</td>
      </tr>
      <tr>
         <td>/meta</td>
         <td>Get your own meta data (swipes left, people seen, etc..)</td>
         <td>{}</td>
         <td>GET</td>
      </tr>
      <tr>
         <td>/report/_id</td>
         <td>Report someone --&gt; There are only a few accepted causes... (see tinder_api.py for options)</td>
         <td>{"cause": cause, "text": explanation}</td>
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
         <td>POST</td>
      </tr>
      <tr>
         <td>/matches/{match id}</td>
         <td>Get a match from its id (thanks <a href="https://github.com/jtabet"> @jtabet </a>)</td>
         <td>{}</td>
         <td>GET</td>
      </tr>
      <tr>
         <td>/message/{message id}</td>
         <td>Get a message from its id (thanks <a href="https://github.com/jtabet"> @jtabet </a>)</td>
         <td>{}</td>
         <td>GET</td>
      </tr>
      <tr>
         <td>/passport/user/reset</td>
         <td>Reset your location to your real location</td>
         <td>{}</td>
         <td>POST</td>
      </tr>
      <tr>
         <td>/passport/user/travel</td>
         <td>Change your swiping location</td>
         <td>{"lat": latitutde, "lon": longitude}</td>
         <td>POST</td>
      </tr>
      <tr>
         <td>/user/{user_id}/common_connections</td>
         <td>Get common connection of a user</td>
         <td>{}</td>
         <td>GET</td>
      </tr>
      <tr>
         <td>/profile/job</td>
         <td>Set job</td>
         <td>{"company":{"id":"17767109610","name":"University of Miami","displayed":true},"title":{"id":"106123522751852","name":"Research Assistant","displayed":true}}</td>
         <td>PUT</td>
      </tr>
      <tr>
         <td>/profile/job</td>
         <td>Delete job</td>
         <td>{}</td>
         <td>DELETE</td>
      </tr>
      <tr>
         <td>/profile/school</td>
         <td>Set school(s)</td>
         <td>{"schools":[{"id":school_id}]}</td>
         <td>PUT</td>
      </tr>
      <tr>
         <td>/profile/school</td>
         <td>Reset school</td>
         <td>{}</td>
         <td>DELETE</td>
      </tr>
      <tr>
         <td>/message/{message_id}/like</td>
         <td>Like a message</td>
         <td>{}</td>
         <td>POST</td>
      </tr>
      <tr>
         <td>/v2/fast-match/preview</td>
         <td>Get the thumbnail image shown in the messages-window (the one showing how many potential matches you have</td>
         <td>{}</td>
         <td>GET</td>
      </tr>
      <tr>
         <td>/giphy/trending?limit={limit}</td>
         <td>Get the trending gifs (tinder uses giphy) accessible in chat</td>
         <td>{}</td>
         <td>GET</td>
      </tr>
      <tr>
         <td>/giphy/search?limit={limit}&query={query}</td>
         <td>Get gifs (tinder uses giphy) based on a search accessible in chat</td>
         <td>{}</td>
         <td>GET</td>
      </tr>
   </tbody>
</table>

### Status Codes
<table>
	<thead>
		<tr>
			<th>Status Code</th>
			<th>Explanation</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>200</td>
			<td>Everything went okay, and the server returned a result (if any).</td>
		</tr>
		<tr>
			<td>301</td>
			<td>he server is redirecting you to a different endpoint. This can happen when a company switches domain names, or an endpoint's name has changed.</td>
		</tr>
		<tr>
			<td>400</td>
			<td>The server thinks you made a bad request. This can happen when you don't send the information the API requires to process your request, among other things.</td>
		</tr>
		<tr>
			<td>401</td>
			<td>The server thinks you're not authenticated. This happens when you don't send the right credentials to access an API</td>
		</tr>
		<tr>
			<td>404</td>
			<td>The server didn't find the resource you tried to access.</td>
	</tbody>
</table>


### Config File
<h5> <strong> facebook_access_token and fb_user_id </strong></h5>

Simply input your facebook username/email and password in your config file. Then, the fb_auth_token.py module will programmatically retrieve your facebook_access_token and fb_user_id. These are then used to generate your tinder_auth_token in tinder_api.py which grants you access to your data! Happy Swiping!
<br>
<h5><strong> SMS Authentication (implemented by <a href='https://github.com/Tagge'>@Tagge</a>) </strong></h5>
SMS authentication is even easier. Just run phone_auth_token.py . You'll be asked your phone number at runtime, you'll then have to type in the code you received by SMS, and it will return your token. We didn't directly implement it in the tinder_api.py because, as opposed to Facebook auth, there's a rate limit to the number of SMS you can receive in an hour (actually 60). It's therefore better to get your token once and use it within its lifetime (24 hours) rather than asking for a new one everytime.<br>
With your token ready, add it to tinder_config_ex.py (value for tinder_token). You're now ready to roll !


<strong> Note: </strong> With the help of <a href=https://github.com/philipperemy/Deep-Learning-Tinder/blob/master/tinder_token.py> philliperemy </a>, I have included a programatic way to acquire your facebook_token. Now, in your config.py just input your facebook username and password.


<strong> Note: </strong> With the help of <a href=https://github.com/gloriamacia> gloriamacia </a>, we added now a jupyter notebook to make the usage even simpler.

<h2> Key Features </h2>

<h3> Match_Info:</h3>
<h4> Creates a local dictionary containing the following keys on each of your matches </h4>

```javascript
{
	  123456: {
	    'messages': [

	    ],
	    'age': 20,
	    'match_id': '123456789123456789',
	    'name': 'Joakim',
	    'photos': [
	      'http://images.gotinder.com/123456789123456789.jpg',
	      'http://images.gotinder.com/123456789123456789.jpg',
	      'http://images.gotinder.com/123456789123456789.jpg',
	      'http://images.gotinder.com/123456789123456789.jpg'
	    ],
	    'message_count': 0,
	    'last_activity_date': '15 days, 16 hrs 46 min 57 sec',
	    'ping_time': '2017-03-11T04:58:56.433Z',
	    'gender': 1,
	    'bio': 'New York Knicks Center',
	    'avg_successRate': 0
	  },
	  56789: {
	    ...
	  }
}
```

<h3> Sorting: </h3>
<h4> Sorting matches by "age", "message_count", and "gender" </h4>

```javascript
[
	  ('123456789123456789',
	  {
	    'messages': [

	    ],
	    'age': 19,
	    'match_id': '123456789123456789abcdefghi',
	    'name': 'Carmelo',
	    'photos': [
	      'http://images.gotinder.com/123456789123456789.jpg',
	      'http://images.gotinder.com/123456789123456789.jpg',
	      'http://images.gotinder.com/123456789123456789.jpg',
	      'http://images.gotinder.com/123456789123456789.jpg'
	    ],
	    'message_count': 0,
	    'last_activity_date': '0 days, 22 hrs 23 min 45 sec',
	    'ping_time': '2017-03-25T23:22:08.954Z',
	    'gender': 1,
	    'bio': 'I do not like to win sometimes', 'avg_successRate': 0.7837966008217391
	    }
	    )
]
```


<h2> The following is no longer available due to Tinder setting their ping_time to a constant date in 2014 and/or the removal of Tinder Social.</h2>
```

<h3> Friends' Pingtimes: </h3>
<h4> friends_pingtimes() will return the following for each facebook friend of yours who has a Tinder
friend_pingtime_by_name("Joakim Noah") will return the pingtime for only that particular friend.
The following is a sample result for friends_pingtimes(): </h4>

`
	"Joakim Noah -----> 15 days, 16 hrs 46 min 57 sec"
	"Carmelo Anthony ------> 0 days, 22 hrs 23 min 45 sec"
	...
`

<h3> Facebook Friends: </h3>
<h4> Given a name, it returns some profile information and their id. Once you have the ID, then you can call api.get_person(id) to get more in-depth information on your friends. </h4>


```javascript

{
	  'Martin Shkreli': {
	    'photo': [
	      {
	        'processedFiles': [
	          {
	            'url': 'https://graph.facebook.com/123456789/picture?height=84&width=84',
	            'height': 84,
	            'width': 84
	          },
	          {
	            'url': 'https://graph.facebook.com/123456789/picture?height=172&width=172',
	            'height': 172,
	            'width': 172
	          },
	          {
	            'url': 'https://graph.facebook.com/123456789/picture?height=320&width=320',
	            'height': 320,
	            'width': 320
	          },
	          {
	            'url': 'https://graph.facebook.com/123456789/picture?height=640&width=640',
	            'height': 640,
	            'width': 640
	          }
	        ]
	      }
	    ],
	    'in_squad': True,
	    'name': 'Martin Shkreli',
	    'user_id': '582bf320452u3yy1217f8'
	  }
}
```
