import sqlite3
import os
import json
import urllib2
import json

def user_details(user_id):
	conn = sqlite3.connect('sqlite3.db')
	cursor = conn.cursor()
	job_titleid = str(user_id);
	query = "Select * from rackerhunt_github_results where id="+user_id
	results = cursor.execute(query)

	for result in results:
		login_name = result[1]

	curl_req = "curl https://api.github.com/users/"+login_name
	user_output = os.popen(curl_req).read()
	js = json.loads(user_output)

	cursor.execute("Delete from rackerhunt_user_details")

	query = "Insert into rackerhunt_user_details values(NULL,'"
	
	github_name = login_name
	if github_name:
		query += login_name + "','"
	else:
		query += "-','"
	
	name = js.get('name')
	if name:
		query += name + "','"
	else:
		query += "-','"
	pic_url = js.get('avatar_url')
	if pic_url:
		query += pic_url + "','"
	else:
		query += "-','"
	repos_url = js.get('repos_url')
	if repos_url:
		query += repos_url + "','"
	else:
	        query += "-','"
	company = js.get('company')
	if company:
		query += company + "','"
	else:
		query += "-','"
	location = js.get('location')
	if location:
		query += location + "','"
	else:
		query += "-','"
	email = js.get('email')
	if email:
		query += email + "','"
	else:
		query += "-','"

	blog_url = js.get('blog')
	if blog_url:
		query += blog_url + "','"
	else:
		query += "-','"

	num_repos = js.get('public_repos')
	if num_repos:
		query += str(num_repos) + "','"
	else:
                query += "-','"
	
	num_followers = js.get('followers')
	if num_followers:
		query += str(num_followers) + "','"
	else:
                query += "-','"

	num_following = js.get('following')
	if num_following:
		query += str(num_following) + "','"
	else:
                query += "-','"
	joined_on = js.get('created_at')
	if joined_on:
		query += joined_on + "','"
	else:
                query += "-','"
	bio = js.get('bio')
	if bio:
		query += bio + "')"
	else:
		query += "-')"

	cursor.execute(query)

	conn.commit()
	conn.close()
