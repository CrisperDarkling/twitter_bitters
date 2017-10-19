import tweepy
from tweepy import OAuthHandler

CONSUMER_KEY = 'Hyuy6deObdj64VuAS2FydPx4J'
CONSUMER_SECRET = 'LuWY7zMXiDmMnWOA2VnppFqDEDFoB00uajpaP2IAV1FvKNxV5b'
OAUTH_TOKEN = '2889039044-UWERBoBLRDQ2kTJhvsBH4jSQhJdU8wCq3Z50Qpr'
OAUTH_TOKEN_SECRET = 'o3yrrv199RtHd9JgetEDQG9og4I7xBM6p4e5y7ikCcasf'

def get_auth():
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    return auth

def get_api():
    auth = get_auth()
    return tweepy.API(auth)