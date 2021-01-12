import os
import tweepy as tw
import pandas as pd

def main(search_words, date_since, x):
    consumer_key = 'Mb97UkSAxLdw3aJGvLvMDWVSz'
    consumer_secret = 'wly2t4wTWWo27z7BNXcdkuDoIfQg7BhIgFw0nmCc9wdhlFEOkW'
    access_key= '1211756547367301121-RTx7PNXabX8V8tMyYSlFFzFRSLGMfe'
    access_secret = 'QCMco5hwdawxpwerpiCDTWm4X8AWOvAVwhKgBT5d3JZvX'

    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tw.API(auth,wait_on_rate_limit=True)

    # search_words = "#trump"
    # date_since = "2020-11-01"

    # Collect tweets
    tweets = tw.Cursor(api.search,
                  q=search_words,
                  lang="en",
                  since=date_since).items(x)
    # tweets


    # Collect a list of tweets
    # [tweet.text for tweet in tweets]
    return tweets
