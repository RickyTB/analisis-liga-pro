from datetime import timedelta
import tweepy
import os
import settings
from utils import load_json
import dateutil.parser
import pandas as pd


def download_tweets(query, until):
  tweets = {}
  for tweet in tweepy.Cursor(api.search, q=query, until=until, lang="es", count=100).items(4000):
    tweets[tweet.id_str] = tweet
  return tweets

def tweet_to_dict(tweet):
  return {
    'id': tweet.id_str,
    'text': tweet.text,
    'created_at': tweet.created_at.strftime('%Y-%m-%d %H:%M'),
    'user_id': tweet.user.id_str,
    'user_name': tweet.user.name,
    'user_screen_name': tweet.user.screen_name,
    'favorite_count': tweet.favorite_count,
    'retweet_count': tweet.retweet_count,
    'source': tweet.source,
    "place": tweet.place.full_name if tweet.place != None else None,
  }

consumer_key = os.getenv('API_KEY')
consumer_secret = os.getenv('API_SECRET_KEY')

auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)

api = tweepy.API(auth)

teams = load_json('data/teams.json')
matches = load_json('data/matches.json')

for match in matches:
  date = dateutil.parser.parse(match['date']) + timedelta(1)
  date = date.strftime('%Y-%m-%d')
  local = teams[str(match['localTeam'])]
  visitor = teams[str(match['visitorTeam'])]
  localTweets = {}
  for keyword in local['keywords']:
    localTweets.update(download_tweets(keyword, date))
  visitorTweets = {}
  for keyword in visitor['keywords']:
    visitorTweets.update(download_tweets(keyword, date))

  localTweets = [tweet_to_dict(tweet) for tweet in localTweets.values()]
  visitorTweets = [tweet_to_dict(tweet) for tweet in visitorTweets.values()]

  localTweets = pd.DataFrame.from_dict(localTweets)
  visitorTweets = pd.DataFrame.from_dict(visitorTweets)

  localTweets.to_csv(f'tweets/equipo_{str(local["id"])}_fecha_{match["tournamentDate"]}.csv', header=True, index=False)
  visitorTweets.to_csv(f'tweets/equipo_{str(visitor["id"])}_fecha_{match["tournamentDate"]}.csv', header=True, index=False)
  
  print(f'Descargados tweets sobre el equipo {local["name"]} en la fecha {match["tournamentDate"]}')
  print(f'Descargados tweets sobre el equipo {visitor["name"]} en la fecha {match["tournamentDate"]}')

print('LISTO')
