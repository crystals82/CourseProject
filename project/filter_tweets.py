import pandas as pd


class tweet_filter:
    def __init__(self):
        self.status = 'on'
    
    def filter_hashtags(tweet_df,schedule_df,lst):
        new_ls = []
        df_list = []
        for tag in lst:
            segmented_df = tweet_df[tweet_df['text'].str.contains(tag)]
            segmented_df['hashtag_used'] = tag
            df_list.append(segmented_df)

        merged = pd.concat(df_list)
        filtered_df = pd.concat([merged.merge(schedule_df,how='left',left_on = 'hashtag_used',right_on = 'hashtag1'), 
                merged.merge(schedule_df,how='left',left_on = 'hashtag_used',right_on = 'hashtag2')])

        return filtered_df

    def keep_only_prematch_tweets(tweet_df):
        final_df = tweet_df[tweet_df['created_at'].dt.tz_localize(None) < tweet_df['clean_datetime_of_match_utc'].dt.tz_localize(None)]
        return final_df

