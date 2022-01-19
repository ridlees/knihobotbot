import scrapper
import time

from dotenv import load_dotenv
import tweepy
import os

load_dotenv()

consumer_key = os.getenv('apiKey')
consumer_secret = os.getenv('apiKeySecret')
clientId = os.getenv('clientId')
clientSecret = os.getenv('clientSecret')
bearer_token = os.getenv('bearerToken')
id = os.getenv('id')

auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)
for tweet in tweepy.Cursor(api.search_tweets, q='tweepy').items(10):
    print(tweet.text)
def send(response):
    print(response)
    
def main():
    "sebevražda je taky možnost, bráško"
    mention = "tweet"
    response = scrapper.main(mention)
    send(response)