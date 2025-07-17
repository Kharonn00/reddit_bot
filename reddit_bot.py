import praw
import config
import time

def bot_login():
	print "Logging in..."

	r = praw.Reddit(username = config.username,
					password = config.password,
					client_id = config.client_id,
					client_secret = config.client_secret,
					user_agent = "Kharoon elephant comment responder v0.1")

	print "Logged in!!"

	return r

def run_bot(r):
	print "Obtaining 25 comments..."
	for comment in r.subreddit('test').comments(limit=25):
		if "elephant" in comment.body:
			print "String with \"elephant\" found in comment" + comment.id
			comment.reply("I also love elephants! [Here] (https://en.wikipedia.org/wiki/File:African_Bush_Elephant.jpg) is an image of one!")
			print "Replied to comment " + comment.id
			
	print "Sleeping for 10 secs"
	time.sleep(10)

r = bot_login()
run_bot(r)