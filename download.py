import tweepy
import os
import settings
from utils import load_json

consumer_key = os.getenv('API_KEY')
consumer_secret = os.getenv('API_SECRET_KEY')

auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)

api = tweepy.API(auth)

teams = load_json('data/teams.json')
matches = load_json('data/matches.json')

print(matches)

#for tweet in tweepy.Cursor(api.search, q='tweepy').items(10):
#    print(tweet.text)
