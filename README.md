# Twitter Data Scraping using Python (Tweepy)

## Overview

This repository contains two Python scripts that allow you to fetch and analyze tweets from Twitter using the **Tweepy** library:

1. **Account.py**: Fetches tweets from a specific user's timeline.
2. **Hashtag.py**: Fetches tweets containing a specific hashtag and performs sentiment analysis.

Both scripts use the **Tweepy** library to interact with the Twitter API and **TextBlob** for sentiment analysis.

---

## Prerequisites

Before you start using the scripts, you need to have the following installed:

- **Python 3.x** (preferably 3.6+)
- **Tweepy**: A Python wrapper for the Twitter API.
- **TextBlob**: A Python library for processing textual data, including sentiment analysis.

You can install the necessary libraries using **pip**:

```bash
pip install tweepy textblob
```

You also need a **Twitter Developer account** and the corresponding **API keys** to access the Twitter API.

---

## Twitter API Credentials

To interact with the Twitter API, you need to create an app on the [Twitter Developer Portal](https://developer.twitter.com/en/apps). Once created, you'll get the following credentials that you need to use in both scripts:

- **Consumer Key**
- **Consumer Secret**
- **Access Token**
- **Access Token Secret**

Replace the placeholder values (`Your-Keys`) in the scripts with your actual credentials.

---

## Scripts

### 1. `Account.py`

This script fetches tweets from a specific Twitter account (timeline) using the `tweepy.Cursor` API. It retrieves a maximum of 3,240 most recent tweets from the account and saves the data to a JSON file.

#### Usage

```bash
python Account.py
```

This will fetch tweets from the Twitter account **realDonaldTrump**. You can change the username in the script to fetch tweets from any other account.

#### Key Features:

- **Fetch tweets from a user’s timeline**.
- Retrieves up to **3,240 tweets** (the maximum allowed by Twitter API).
- Saves tweet data in **JSON format**.

#### Example:
```python
get_all_tweets("realDonaldTrump")
```

### 2. `Hashtag.py`

This script fetches tweets containing a specific hashtag and performs sentiment analysis using **TextBlob**. The tweets are saved to a CSV file with the following information: tweet content, sentiment score, and user details.

#### Usage

```bash
python Hashtag.py
```

This will search for tweets containing the hashtag `#Apple`. You can modify the hashtag in the `q` parameter to search for other hashtags.

#### Key Features:

- **Fetch tweets by hashtag**.
- **Sentiment analysis** using **TextBlob**.
- Saves tweet data (including sentiment) to a **CSV file**.

#### Example:
```python
for tweet in tweepy.Cursor(api.search, q="#Apple", count=100, lang="en", tweet_mode='extended', since="2018-01-01").items(maxTweets):
```

---

## How the Code Works

### 1. `Account.py` Explanation:

- **Authentication**: The script authenticates using the Twitter API credentials.
- **Fetching Tweets**: The `get_all_tweets()` function uses `tweepy.Cursor` to fetch tweets from a user's timeline (up to 3,240 tweets).
- **Saving to JSON**: The tweet data is saved into a **JSON** file (`tweet.json`).

### 2. `Hashtag.py` Explanation:

- **Authentication**: The script authenticates using the Twitter API credentials.
- **Fetching Tweets by Hashtag**: It uses `tweepy.Cursor` to search for tweets containing the specified hashtag (`#Apple` in this case).
- **Cleaning Tweet Text**: The `clean_tweet()` function removes special characters and links from the tweet text.
- **Sentiment Analysis**: The `analyze_sentiment()` function uses **TextBlob** to determine whether the tweet is positive, negative, or neutral based on its sentiment score.
- **Saving to CSV**: The tweet data, along with sentiment analysis and user details, is saved into a **CSV** file (`tweets.csv`).

---

## Example Outputs

- **Account.py Output**: A **JSON** file containing tweet objects, including information like tweet content, creation time, user details, and more.
  
  ```json
  {
    "created_at": "2025-03-24T00:00:00Z",
    "id": 123456789012345678,
    "full_text": "This is a tweet",
    "user": {
      "screen_name": "realDonaldTrump",
      "followers_count": 1234567
    },
    "favorite_count": 100,
    "retweet_count": 50,
    ...
  }
  ```

- **Hashtag.py Output**: A **CSV** file containing tweet information and sentiment analysis:

  ```csv
  Created At | Tweet Text | Sentiment | Contributors | Truncated | Is Quote Status | Tweet ID | Source | Favorite Count | Retweet Count | ...
  2025-03-24 | This is a tweet #Apple | 1 | None | False | False | 1234567890 | Twitter Web App | 100 | 50 | ...
  ```

  - Sentiment is represented as:
    - `1`: Positive
    - `0`: Neutral
    - `-1`: Negative

---

## License

This project is licensed under the **MIT License** - see https://opensource.org/license/mit for details.

---

## Conclusion

These scripts provide a simple yet powerful way to collect Twitter data based on a user's account or hashtag, perform sentiment analysis, and store the results for further analysis. Make sure you have your Twitter API credentials ready to start using the scripts.
