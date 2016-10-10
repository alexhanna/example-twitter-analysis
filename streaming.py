from slistener import SListener
import json
import time
import tweepy
import sys

#authObj = json.loads( open('keys.json', 'r').read() )

## authentication
access_token = "FGw5OIcXnaS9w4E1ApbElbxjxkSGNRtD6LENKeMw78"
access_token_secret = "xNomP4p90I1oWCLp3cAhH0BwIvPu0l3y2YvxpvthNM2Y4"
consumer_key = "jdlBbsGOvrceuji38Yu5MA"
consumer_secret = "FGw5OIcXnaS9w4E1ApbElbxjxkSGNRtD6LENKeMw78"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api  = tweepy.API(auth)

## set up words to track
track = ['trump', 'clinton']

listen = SListener(api, 'election2016')
stream = tweepy.Stream(auth, listen)

print("Streaming started...")

stream.filter(track = track)

## alternative endpoints for filter include follow and locations
## https://dev.twitter.com/streaming/reference/post/statuses/filter