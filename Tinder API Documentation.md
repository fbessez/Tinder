Tinder API Documentation -- 2017

First off, I want to give a shoutout to @rtt who initially posted the Tinder API Documentation that I found most of these endpoints on

**Note: This was written in February 2017. API might be outdate.**

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
			<td>{'facebook_token': <TOKEN>, 'facebook_id': <ID>}</td>
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
			<td>{"message": <TEXT GOES HERE>}</td>
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
			<td>{"cause": <CAUSE>}</td>
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


























