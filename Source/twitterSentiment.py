#import tweepy library which helps us to access twitter api
import tweepy
#import TextBlob from textblob
from textblob import TextBlob

#make four variables which stores your keys as in string
#you can get these from your twitter api registered dashboard
consumer_key='<your consumer key>'
consumer_secret='<your consumer secret>'

access_token='<your access token>'
access_token_secret='<your access token secret>'
#create a varable which helps as to authicate with twitter api
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
#set access foryour access_token
auth.set_access_token(access_token,access_token_secret)
#make main variable which auth with twitter api
api=tweepy.API(auth)
#make a variable which stores all the tweets which contains the word you are searching for
#here i search all the tweets which contain the word cricket
public_tweets=api.search('cricket')

#make a for loop and access all the tweets one by one
for tweet in public_tweets:
    #print the tweets if you want
    print(tweet.text)
    #make a variable which stores a list which contains the split words using TextBlob.
    analysis=TextBlob(tweet.text)
    #print sentiment of each using sentiment
    print(analysis.sentiment)