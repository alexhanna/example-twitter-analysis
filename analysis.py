import glob
import json
import pandas as pd
import numpy as np

tweets = []
files  = list(glob.iglob('election2016*.json'))
for f in files:
    tweets_json = open(f, 'r', encoding = 'utf-8').read().split("\n")

    ## remove empty lines
    tweets_json = list(filter(len, tweets_json))

    ## try to parse each tweet
    for tweet in tweets_json:
        try:
            tweet_obj = json.loads(tweet)
            tweets.append(tweet_obj)
        except:
            ## fails to parse
            pass

## create pandas DataFrame for further analysis
df_tweet = pd.DataFrame(tweets)