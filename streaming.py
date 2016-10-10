from slistener import SListener
import json
import time
import tweepy
import sys

authObj = json.loads( open('keys.json', 'r').read() )

## authentication
access_token = authObj['access_token']
access_token_secret = authObj['access_token_secret']
consumer_key = authObj['consumer_key']
consumer_secret = authObj['consumer_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api  = tweepy.API(auth)

## set up words to track
track = ['trump', 'clinton']

listen = SListener(api, 'election2016')
stream = tweepy.Stream(auth, listen)

print("Streaming started...")

try: 
    stream.filter(track = track)
except:
    print("error!")
    stream.disconnect()
