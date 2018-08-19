#import tweepy library which helps us to access twitter api
import tweepy
#import TextBlob from textblob
from textblob import TextBlob
# Each word in the lexicon has scores for:
# 1)     polarity: negative vs. positive    (-1.0 => +1.0)
# 2)     subjectivity: objective vs. subjective (+0.0 => +1.0)
# 3)    intensity: modifies next word?      (x0.5 => x2.0)

#make four variables which stores your keys as in string
#you can get these from your twitter api registered dashboard
consumer_key='TAnYsf1oMVSqJcqmSgTUaaxFm'
consumer_secret='1OIMTW57hTaZffektXBwA7PFvwsFu2WsS6KssPiFHHrbNP12lU'

access_token='61872867-xFsISv0Q1fM2HfK8O0kKf8CLjJX093upSD9MyWqz1'
access_token_secret='oKlbTKBSP6j8wE0TtMSXm7EdfJk3CX2kkdeOwO6xTTjjh'
#create a varable which helps as to authicate with twitter api
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
#set access foryour access_token
auth.set_access_token(access_token,access_token_secret)
#make main variable which auth with twitter api
api=tweepy.API(auth)
#make a variable which stores all the tweets which contains the word you are searching for
#here i search all the tweets which contain the word cricket
public_tweets=api.search('Renzi')

# Put sentiments in arrays
polarity = []
subjectivity = []

#make a for loop and access all the tweets one by one
for tweet in public_tweets:
    #print the tweets if you want
    #print(tweet.text)
    #make a variable which stores a list which contains the split words using TextBlob.
    analysis=TextBlob(tweet.text)
    
    #print sentiment of each using sentiment
    
    #print(analysis.sentiment)
    #print(analysis.polarity)
    polarity.append(analysis.polarity)
    #print(analysis.subjectivity)
    subjectivity.append(analysis.subjectivity)

print sum(polarity)/len(polarity)
print sum(subjectivity)/len(subjectivity)