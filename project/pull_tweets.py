from bsi_sentiment.twitter import search_tweets_sn
import datetime
import pandas as pd

class historical_tweets:
 
    def __init__(self):
        self.status = 'on'

    def get_world_cup_tweets(tweet_num):
        new_tweets = search_tweets_sn(
  q="#T20WorldCup",
  since="2021-09-01",
  until="2021-11-09",
  lang="en",
  max_tweets=tweet_num
)
        return new_tweets

    def build_df(tweet_object):
        t20_dict = []
        for item in tweet_object :

            mined = {'tweet_id': item.id,
            'username': item.username,
            'text': item.text,
            'tweet_link' : item.permalink,
            'created_at': item.date,
            'mined_at': datetime.datetime.now()}

            t20_dict.append(mined)
            t20_df = pd.DataFrame(t20_dict)
        return t20_df