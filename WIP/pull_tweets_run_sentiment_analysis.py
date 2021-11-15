import re

import tweepy as tw
import metapy as meta
import pandas as pd
from textblob import TextBlob

consumer_key = "5TwiO8dEFQL7pMLQxxrWWSVDM"
consumer_secret = "LrjzXmJP8bst2c6eTc7rzjjh4kS14bOj9HoMwLGBOwaxSfDpKY"
auth = tw.OAuthHandler(consumer_key, consumer_secret)
api = tw.API(auth)

def percentage(part, whole):
  return 100 * float(part)/float(whole)
keywords = "T20WorldCup+Predict -filter:retweets"

# World cup started Oct 17, 2021 and Final is on Nov 14, 2021

# date_since = "2021-10-15"
# retrieving tweets
tweets = tw.Cursor(api.search, keywords, "en", since="2021-10-10", tweet_mode="extended").items(1000)
# print(tweets.full_text)

tweets_df= []
# Iterate and Analyse the tweets
positive = 0
negative = 0
neutral = 0
polarity = 0
subjectivity = 0
for tweet in tweets:
    #print (tweet)
    # print(tweet.full_text)
  clean_tweet = " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", tweet.full_text).split())
  #print(clean_tweet)
  user_loc = [tweet.user.screen_name, tweet.user.location, tweet.created_at, clean_tweet]
  #print(user_loc)
 # tweets_df = pd.DataFrame(data=user_loc, columns=['user', 'location', 'created_date', 'clean_tweet'])

  analysis = TextBlob(clean_tweet)
  sentiment = analysis.sentiment.polarity
  sentiment1 = analysis.sentiment.subjectivity
  polarity = sentiment
  subjectivity = sentiment1
  user_loc.append(polarity)
  user_loc.append(subjectivity)

  tweets_df.append(user_loc)

  if sentiment < 0:
     negative += 1
  elif sentiment == 0:
    neutral += 1
  elif sentiment > 0:
    positive += 1
#print (tweets_df)

print (analysis.sentiment)
positivePercentage = float(format(percentage(positive, 1000), '.2f'))
negativePercentage = float(format(percentage(negative, 1000), '.2f'))
neutralPercentage  = float(format(percentage(neutral, 1000), '.2f'))
polarityPercentage = float(format(percentage(polarity, 1000), '.2f'))

#print(type(positivePercentage))
#print(positivePercentage)
print('Positive Sentiment: ' + str(positivePercentage))

if polarityPercentage < 0.00:
  print('Polarity Negative')
elif polarityPercentage == 0:
  print('Polarity Neutral')
elif polarityPercentage > 0.00:
  print('Polarity Positive')

print('Polarity: ' + str(polarityPercentage))

df = pd.DataFrame(tweets_df)
print (df)
df.to_csv('tweepy_dataset.csv', encoding='utf-8')