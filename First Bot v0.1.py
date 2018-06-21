"""
Project Name - StayInTheLoop
Description  - Scrape /r/outoftheloop, and use selenium with google trends to scrape most frequently searched posts contents
Author       - Bilaal Hussain
Date         - 5/15/2018
"""

import praw
import nltk
import re
from nltk.corpus import stopwords
import time
from selenium import webdriver
reddit = praw.Reddit('bot1', user_agent='First Bot v0.1')
subreddit = reddit.subreddit("outoftheloop")
chrome_path = "P:\Development\Python\First Reddit Bot\StayInTheLoop\chromedriver.exe"
google_trends = "https://trends.google.com/trends/?geo=US"
#content = reddit.get_content()
#Data storage

post_ids = []
post_titles = []
post_responses = []


#Query limit
limit = 5
sleep_time = 300


current_iterations = 0

#Purpose: filter_dictionary_words(text): Returns text with all common words from the Unix usr/share/dict/words dictionary
#	removed. Uses this to find any words that don't appear in the english language.
#Contract: ListOf(String) -> ListOf(String)
#This will often find the most important words in a reddit post. Often referring to the subject.
def filter_dictionary_words(text):
    text_vocab = set(w.lower() for w in text if w.isalpha())
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    unusual = text_vocab - english_vocab
    return sorted(unusual)

#Purpose: filter_dictionary_words(text): Returns text with high frequency words with minimal lexical context filtered out
#Contract: ListOf(String) -> ListOf(String)
#This is a less aggressive version of the filter_dictionary_words function
def filter_common_words(text):
    text_vocab = set(w.lower() for w in text if w.isalpha())
    common_vocab = set(w.lower() for w in nltk.corpus.stopwords.words('english'))
    uncommon = text_vocab - common_vocab
    return sorted(uncommon)

def test_significance(words):
	driver = webdriver.Chrome(chrome_path)
	driver.get(google_trends)
	element = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/ng-include/div/div[2]/div/div')
	for word in words:
		element.send_keys(word + " ")
		driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/md-content/div/div/div[1]/trends-widget/ng-include/widget/div/div/div/widget-actions/div/button[1]/i').click

	
while(True):
	for post in subreddit.hot(limit=5):
		# if it is a question, store the title and score
		if post.id not in post_ids:
			#debugging
			print( '\nQuestion: ', post.title)
			#print( 'Score: ', post.score)
			post_ids.append(post.id)
			post_titles.append(post.title)
			print(post_titles[-1])			
			nouns = filter_common_words(post_titles[-1].split())
			print(nouns)

"""
while (True):
	for post in subreddit.hot(limit=5):
		if post.id not in post_ids:
			#debugging
			print '\nQuestion: ', post.title
			print 'Score: ', post.score
			post_ids.append(post.id)
			post_titles.append(post.title)
			nouns = filter_common_words(post_titles[-1].split())		
		
			post_comments = post.comments
			top_comment = ''
			
			for comment in post_comments:
				comment_text = post_comment.body
				comment_score = post_comment.score
				#TODO: Fix janky way of finding highest score. Look for API call that finds top post score
				if (comment_score > top_score):
					top_comment = comment_text
					top_score = comment.score
			post_responses.append(top_comment) 			# TODO: Process posts for better responses
			current_iterations += 1

			# print the status
			print "Iterations: ", current_iterations,
			time.sleep(delay_slot)
			
			reddit.redditor('the_undoxxed').message(top_comment, post.title) 	#TODO: Create ALF for this function mapping functions to post/comment pairs
																					#TODO: Create mailing list
			if (current_iterations >= max_iterations):
				break
	time.sleep(sleep_time)
	# reached if max_iterations is met or no more content
	break
"""