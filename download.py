import tweepy
import os
import settings
from utils import load_json
import dateutil.parser
import pandas as pd


def download_tweets(query, until):
  tweets = {}
  for tweet in tweepy.Cursor(api.search, q=query, lang="es", count=100).items():
    tweets[tweet.id_str] = tweet
  print(query)
  print(len(tweets.values()))
  return tweets

def tweet_to_dict(tweet):
  return {
    'id': tweet.id_str,
    'text': tweet.text,
    'created_at': tweet.created_at,
    'user_id': tweet.user.id_str,
    'user_name': tweet.user.name,
    'user_screen_name': tweet.user.screen_name,
  }

consumer_key = os.getenv('API_KEY')
consumer_secret = os.getenv('API_SECRET_KEY')

auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)

api = tweepy.API(auth)

teams = load_json('data/teams.json')
matches = load_json('data/matches.json')

for match in matches:
  date = dateutil.parser.parse(match['date'])
  date = date.strftime('%Y-%m-%d %H:%M')
  local = teams[str(match['localTeam'])]
  visitor = teams[str(match['visitorTeam'])]
  localTweets = {}
  for keyword in local['keywords']:
    localTweets.update(download_tweets(keyword, date))
    #print(localTweets)
  visitorTweets = {}
  for keyword in visitor['keywords']:
    visitorTweets.update(download_tweets(keyword, date))
    #print(visitorTweets)

  localTweets = [tweet_to_dict(tweet) for tweet in localTweets.values()]
  visitorTweets = [tweet_to_dict(tweet) for tweet in visitorTweets.values()]

  localTweets = pd.DataFrame.from_dict(localTweets)
  visitorTweets = pd.DataFrame.from_dict(visitorTweets)

  localTweets.to_csv(f'tweets/equipo_{str(local["id"])}_fecha_{match["tournamentDate"]}.csv', header=True, index=False)
  visitorTweets.to_csv(f'tweets/equipo_{str(visitor["id"])}_fecha_{match["tournamentDate"]}.csv', header=True, index=False)
  
  print(f'Descargados tweets sobre el equipo {local["name"]} en la fecha {match["tournamentDate"]}')
  print(f'Descargados tweets sobre el equipo {visitor["name"]} en la fecha {match["tournamentDate"]}')

print('LISTO')
