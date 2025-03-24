#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tweepy
import json

# Twitter API credentials
consumer_key = "Your-Keys"
consumer_secret = "Your-Keys"
access_key = "Your-Keys"
access_secret = "Your-Keys"


def get_all_tweets(screen_name):
    # Twitter only allows access to a user's most recent 3240 tweets with this method
    
    # authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # initialize a list to hold all the tweepy Tweets
    alltweets = []

    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name=screen_name, count=200)

    # save most recent tweets
    alltweets.extend(new_tweets)

    # save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    # keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        # all subsequent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)

        # save most recent tweets
        alltweets.extend(new_tweets)

        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print(f"...{len(alltweets)} tweets downloaded so far")

    # write tweet objects to JSON
    with open('tweet.json', 'w', encoding='utf-8') as file:
        print("Writing tweet objects to JSON, please wait...")
        for status in alltweets:
            json.dump(status._json, file, ensure_ascii=False, indent=4)

    print("Done")


if __name__ == '__main__':
    # pass in the username of the account you want to download
    get_all_tweets("realDonaldTrump")
