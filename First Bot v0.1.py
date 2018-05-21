"""
Project Name - First Reddit Bot
Description  - Attempting Side project for 2a coop term LOOOL
Author       - Bilaal Hussain
Date         - 5/19/2018
Time         - 3:20 PM
"""

import praw

reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit("outoftheloop")

for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("----------------------------\n")
