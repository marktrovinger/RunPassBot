##
# tweet.py - Main file for the twitter bot, handles all stages of tweeting a live game.
#
## 

import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

