import sqlite3
import os
import json
import urllib2
import json



def github_results(job_id):

	conn = sqlite3.connect('sqlite3.db')
	cursor = conn.cursor()
	job_titleid = str(job_id);
	query = "Select * from rackerhunt_jobs where id="+job_titleid
	print 'query',query
	results = cursor.execute(query)

	for result in results:
    		job_title = str(result[1])
    		location = str(result[2])
    		skills = str(result[3])
	conn.close()

	# Parse skills
	languages = skills.split(',')
	language = languages[0]
	for i in range(1,len(languages)):
    		language += "%3A" + languages[i]

	# Create curl requests
	curl_command = "curl -H 'Accept: application/vnd.github.preview.text-match+json' https://api.github.com/search/users?q=language:" 
	curl_command += language + "+location:" + location
	curl_command += "&sort=followers"
#	print 'curl_command', curl_command
	os.system(curl_command)
	# JSON Parsing
	output = os.popen(curl_command).read()
	js = json.loads(output)

	profiles = js['items']
	user_list = []
	for profile in profiles:
    		name = profile['login']
    		user_list.append(name)


	conn = sqlite3.connect('sqlite3.db')
	cursor = conn.cursor()
	cursor.execute("Delete from rackerhunt_github_results")
	# user details
	
	#user = user_list[0]
	curl_user_details1 = "curl https://api.github.com/users/"
	count = 0
	for user in user_list:
	    count += 1
	    if count <= 5:
	        curl_user_details1 = "curl https://api.github.com/users/"
		curl_user_details1 += user
		#print 'curl_user_details1', curl_user_details1 
		os.system(curl_user_details1)
		# again parse based on the required fields
		user_output = os.popen(curl_user_details1).read()
		js = json.loads(user_output)
		name = user
		followers = 0
		pic_link = ' '
		email = '-'
		score = '1'
		#if js.get('name'):
		#	name = js['name']
		if js.get('followers'):
			followers = js['followers']
		if js.get('avatar_url'):	
			pic_link = js.get('avatar_url')
		if js.get('email'):
			email = js['email']
		query="Insert into github_results values ('"+name+"','"+pic_link+"',"+str(followers)+",'"+score+"','"+email+"')"
		print query
		cursor.execute("Insert into rackerhunt_github_results values (NULL,'"+name+"','"+pic_link+"',"+str(followers)+",'"+score+"','"+email+"')")
		curl_user_details1 = ""
	
	conn.commit()
	conn.close()
