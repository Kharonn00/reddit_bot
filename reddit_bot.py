import praw
import config
import time
import os
import requests

def bot_login():
    print("Logging in...")

    reddit = praw.Reddit(
        username=config.username,
        password=config.password,
        client_id=config.client_id,
        client_secret=config.client_secret,
        user_agent="Kharoon joke comment responder v0.1"
    )

    print("Logged in!")
    return reddit


def run_bot(reddit, replied_to):
    print("Checking latest comments...")

    for comment in reddit.subreddit('test').comments(limit=25):

        if "!joke" in comment.body.lower() and comment.id not in replied_to and comment.author != reddit.user.me():
            print(f'String with "!joke" found in comment {comment.id}')

            # Try to get a joke from the API
            try:
                response = requests.get('http://api.icndb.com/jokes/random', timeout=5)
                response.raise_for_status()  # raises error for bad responses
                joke = response.json()['value']['joke']
            except Exception as e:
                joke = "Oops! Couldn't fetch a Chuck Norris joke right now. Try again later."
                print(f"Error fetching joke: {e}")

            comment_reply = f"You requested a Chuck Norris !joke. Here it is:\n\n> {joke}"

            try:
                comment.reply(comment_reply)
                print(f"Replied to comment {comment.id}")
                replied_to.add(comment.id)
            except Exception as e:
                print(f"Error replying to comment {comment.id}: {e}")

    # Without API
    # _______________
    #
    # for comment in reddit.subreddit('test').comments(limit=25):
    #
    #     if "joke" in comment.body.lower() and comment.id not in replied_to and comment.author != reddit.user.me():
    #         print(f"Found 'joke' in comment {comment.id}")
    #         comment.reply("I also love jokes! [Here](https://yourwebsite.com/jpg.jpg) is an image of one!"
    #
    #         print(f"Replied to comment {comment.id}")
    #         replied_to.add(comment.id)


def get_saved_comments():
    if not os.path.isfile("comment_replied_to.txt"):
        return set()

    with open("comment_replied_to.txt", "r") as f:
        ids = f.read().splitlines()

    return set(ids)


def save_replied_comments(replied_to):
    with open("comment_replied_to.txt", "w") as f:
        for comment_id in replied_to:
            f.write(comment_id + "\n")

if __name__ == "__main__":
    reddit = bot_login()
    replied_to = get_saved_comments()

    while True:
        run_bot(reddit, replied_to)
        save_replied_comments(replied_to)
        print("Sleeping for 10 seconds...\n")
        time.sleep(10)
