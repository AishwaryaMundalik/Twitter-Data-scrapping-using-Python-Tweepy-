import tweepy
import csv
from textblob import TextBlob
import re

# Maximum number of tweets to fetch
maxTweets = 10000

def clean_tweet(tweet):
    """
    Utility function to clean the text in a tweet by removing 
    links and special characters using regex.
    """
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def analyze_sentiment(tweet):
    """
    Utility function to classify the polarity of a tweet
    using TextBlob.
    """
    analysis = TextBlob(clean_tweet(tweet))
    if analysis.sentiment.polarity > 0:
        return 1
    elif analysis.sentiment.polarity == 0:
        return 0
    else:
        return -1


# Input your credentials here
consumer_key = 'Your-Keys'
consumer_secret = 'Your-Keys'
access_token = 'Your-Keys'
access_token_secret = 'Your-Keys'

# Authenticate and set up Tweepy API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# Open/Create a CSV file to append data
with open('tweets.csv', 'a', newline='', encoding='utf-8') as csvFile:
    csvWriter = csv.writer(csvFile, delimiter='|')

    # Writing the header row (optional, to include column names)
    csvWriter.writerow([
        "Created At", "Tweet Text", "Sentiment", "Contributors", "Truncated", "Is Quote Status",
        "In Reply To Status ID", "Tweet ID", "Source", "Favorite Count", "Retweet Count", "Geo", 
        "Coordinates", "Entities", "User Follow Request Sent", "Has Extended Profile", 
        "Profile Use Background Image", "User Time Zone", "User ID", "User Description", 
        "User Verified", "User Profile Image", "User Followers Count", "User Protected", 
        "User ID Str", "User Listed Count", "User Location", "User Following"
    ])

    for tweet in tweepy.Cursor(api.search, q="#Apple", count=100, lang="en", tweet_mode='extended', since="2018-01-01").items(maxTweets):
        if not tweet.retweeted and 'RT @' not in tweet.full_text:
            csvWriter.writerow([
                tweet.created_at, 
                clean_tweet(tweet.full_text).replace('\n', '').replace('\r', '').replace('|', ''), 
                analyze_sentiment(tweet.full_text),
                tweet.contributors, 
                tweet.truncated, 
                tweet.is_quote_status, 
                tweet.in_reply_to_status_id,  
                tweet.id, 
                tweet.source,
                tweet.favorite_count,
                tweet.retweet_count, 
                tweet.geo,
                tweet.coordinates,
                tweet.entities,
                tweet.author.follow_request_sent,
                tweet.author.has_extended_profile,
                tweet.author.profile_use_background_image,
                tweet.author.time_zone,
                tweet.author.id,
                tweet.author.description, 
                tweet.author.verified,
                tweet.author.profile_image_url_https,
                tweet.author.followers_count,
                tweet.author.protected,
                tweet.author.id_str,
                tweet.author.listed_count,
                tweet.author.location,
                tweet.author.following
            ])
