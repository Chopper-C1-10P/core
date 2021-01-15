import praw

from helpers.config import config

client_id = config("config.json", "reddit_client_id")
client_secret = config("config.json", "reddit_client_secret")
user_agent = config("config.json", "reddit_user_agent")

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent
    )
