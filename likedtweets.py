"""
This script will obtain a random tweet that you recently like and display it
to you on the console.
"""
import json
import random
import tweepy


"""
Read the contents of a JSON file; the file is assumed to contain OAuth
credentials.
"""
def read_credentials(filename):
    with open(filename, "r") as f:
        creds = json.loads(f.read())
    return creds

"""
Given a JSON object with OAuth credential information this function will
return an object that has access to the Twitter API.
"""
def get_api_connection(creds):
    auth = tweepy.OAuthHandler(creds['consumer_key'], creds['consumer_secret'])
    auth.set_access_token(creds['access_token'], creds['access_token_secret'])
    api = tweepy.API(auth)
    return api

"""
Obtains the url associated with a tweet, if that information is available.
"""
def get_tweet_url(tweet):
    try:
        return tweet.entities['media'][0]['url']
    except:
        return None

"""
Given a connection to the Twitter API this function will obtain the text and
url associated with a random tweet that you recently favorited.
"""
def get_random_favorite_tweet_details(api):
    favorite_tweets = api.favorites()
    tweet = random.choice(favorite_tweets)
    return (tweet.text, get_tweet_url(tweet))

"""
Format the text and url associated with a Tweet so it can be printed to the
screen.
"""
def format_output(tweet_text, tweet_url):
    
    return """
    Check this out!:

    =====
    Tweet
    =====
    {}

    =====
    URL 
    =====
    {}
    """.format(tweet_text, tweet_url)

if __name__ == "__main__":
    creds = read_credentials("cred.json")
    api = get_api_connection(creds)
    tweet_text, tweet_url = get_random_favorite_tweet_details(api)
    output = format_output(tweet_text, tweet_url)
    print(output)
