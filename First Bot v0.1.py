"""
Project Name - StayInTheLoop
Description  - Scrape /r/outoftheloop, and use selenium with google trends to scrape most frequently searched posts contents
Author       - Bilaal Hussain
Date         - 5/15/2018
"""

import praw

reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit("outoftheloop")

for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("----------------------------\n")
