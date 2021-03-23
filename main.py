import tweepy
import os
import settings

consumer_key = os.getenv('API_KEY')
consumer_secret = os.getenv('API_SECRET_KEY')

auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)

api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search, q='tweepy').items(10):
    print(tweet.text)