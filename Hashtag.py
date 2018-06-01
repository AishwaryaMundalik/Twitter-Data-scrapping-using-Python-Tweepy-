import tweepy
import csv
import pandas as pd
from textblob import TextBlob
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')

maxTweets=10000


def clean_tweet(tweet):
    '''
    Utility function to clean the text in a tweet by removing 
    links and special characters using regex.
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def analize_sentiment(tweet):
    '''
    Utility function to classify the polarity of a tweet
    using textblob.
    '''
    analysis = TextBlob(clean_tweet(tweet))
    if analysis.sentiment.polarity > 0:
        return 1
    elif analysis.sentiment.polarity == 0:
        return 0
    else:
        return -1



####input your credentials here
consumer_key = 'gOYTBFrUckDnnd8CpYKo4pOc8'
consumer_secret = 'kOLlZA9BKqdJk8moupsnCeaz0OPwjC1YXwvbFHQJx1I1cYChV7'
access_token = '805231072086724608-QVSifDJxm0LCzoNA6jVnkG5kpiVBkWk'
access_token_secret = '1heXdob6dKg6qvjqOQZXwB8Ahndwqxl8ipwbIWTMVLR19'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('ua.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile,delimiter='|')

for tweet in tweepy.Cursor(api.search,q="#Apple",count=100,lang="en",tweet_mode='extended',since="2018-01-01").items(maxTweets):
    if (not tweet.retweeted) and ('RT @' not in tweet.full_text):
       csvWriter.writerow([tweet.created_at, clean_tweet(tweet.full_text).replace('\n', '').replace('\r', '').replace('|',''),analize_sentiment(tweet.full_text), 
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
tweet._api,
tweet.author.follow_request_sent,
tweet.author.has_extended_profile,
tweet.author.profile_use_background_image,
tweet.author.time_zone,tweet.author.id,
tweet.author.description.encode,
tweet.author._api,
tweet.author.verified,
tweet.author.profile_text_color,
tweet.author.profile_image_url_https,
tweet.author.profile_sidebar_fill_color,
tweet.author.is_translator,
tweet.author.geo_enabled, 
tweet.author.entities, 
tweet.author.followers_count,
tweet.author.protected,
tweet.author.id_str,
tweet.author.default_profile_image,
tweet.author.listed_count,
tweet.author.lang,
tweet.author.utc_offset,
tweet.author.statuses_count,
tweet.author.profile_background_color,
tweet.author.friends_count,
tweet.author.profile_link_color,
tweet.author.profile_image_url,
tweet.author.notifications,
tweet.author.default_profile,
tweet.author.profile_background_image_url_https,
tweet.author.profile_background_image_url,
tweet.author.name.encode,
tweet.author.is_translation_enabled,
tweet.author.profile_background_tile,
tweet.author.favourites_count,
tweet.author.screen_name,
tweet.author.url,
tweet.author.created_at,
tweet.author.contributors_enabled,
tweet.author.location.encode,
tweet.author.profile_sidebar_border_color,
tweet.author.translator_type,
tweet.author.following])
