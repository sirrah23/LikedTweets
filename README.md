# LikedTweets
Randomly obtain a tweet that you recently liked.

## Prerequisites
It is assumed that:

- You have [pipenv](https://docs.pipenv.org/) installed on your machine
- You have created an application on the [Twitter dashboard](https://apps.twitter.com/)

## Setup
```
git clone https://github.com/sirrah23/LikedTweets.git
cd LikedTweets
pipenv install
touch cred.json
```

Populate the `cred.json` file with your Twitter OAuth credentials. The
following keys are expected to be in the file:

- consumer_key 
- consumer_secret
- access_token
- access_token_secret

## Run
```
pipenv shell
python likedtweets.py
```