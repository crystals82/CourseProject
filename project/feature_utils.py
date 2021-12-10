import pandas as pd
from textblob import TextBlob

class feature_utilities:
    def __init__(self):
        self.status = 'on'
    
    def polarity_calc(text):
        try:
            return TextBlob(text).polarity
        except:
            return None
    
    def subjectivity_calc(text):
        try:
            return TextBlob(text).subjectivity
        except:
            return None

    def clean_training_set(pre_df,post_df):
        comb = post_df.merge(pre_df,how='left',left_on = 'Tweet date',right_on = 'created_at')    
        clean_df = comb[['Match#' ,'tweet_id_x','text_x','Tweet date','y_is_prediction','created_at','hashtag_used','clean_datetime_of_match_utc']]
        clean_df['text'] =  clean_df['text_x']
        return clean_df
