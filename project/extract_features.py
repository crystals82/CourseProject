import pandas as pd
from feature_utils import feature_utilities

class feature_extraction:
    def __init__(self):
        self.status = 'on'

    def build_feature_set(df):
        start_time = pd.to_datetime(df['created_at'].astype(str)) 
        end_time = pd.to_datetime(df['clean_datetime_of_match_utc'].astype(str))
        df['tweet_mins_before_match'] = end_time.sub(start_time).dt.total_seconds().div(60)
        df['lower_text'] = df['text'].str.lower()
        df['contains_will_win'] = df.text.str.contains('will win')
        df['contains_will_defeat'] = df.text.str.contains('will defeat')
        df['contains_will_beat'] = df.text.str.contains('will beat')
        df['contains_will_lose'] = df.text.str.contains('will lose')
        df['contains_will_score'] = df.text.str.contains('will score')
        df['contains_winner'] = df.text.str.contains('winner')
        df['contains_predict'] = df.text.str.contains('predict')
        df['contains_favorite'] = df.text.str.contains('favorite')
        df['contains_should'] = df.text.str.contains('should')
        df['contains_win'] = df.text.str.contains('win')
        df['contains_champion'] = df.text.str.contains('champion')
        df['contains_victor'] = df.text.str.contains('victor')
        df['contains_upper_hand'] = df.text.str.contains('upper hand')
        df['contains_who'] = df.text.str.contains('who')
        df['contains_advantage'] = df.text.str.contains('advantage')
        df['contains_lost'] = df.text.str.contains('lost')
        df['contains_to_win'] = df.text.str.contains('to win')
        df['contains_contend'] = df.text.str.contains('contend')
        df['contains_outclassed'] = df.text.str.contains('outclassed')
        df['contains_defeat'] = df.text.str.contains('defeat')
        df['contains_with_win'] = df.text.str.contains('with win')
        df['contains_bat_first'] = df.text.str.contains('bat first')
        df['contains_quotes'] = df.text.str.contains('""')
        df['contains_toss'] = df.text.str.contains('toss')
        df['contains_won_the_toss'] = df.text.str.contains('won the toss')
        df['contains_bowl_first'] = df.text.str.contains('bowl first')
        df['contains_win_by'] = df.text.str.contains('win by')
        df['polarity'] = df['text'].apply(feature_utilities.polarity_calc)
        df['subjectivity'] = df['text'].apply(feature_utilities.subjectivity_calc)
        final_x = df[['tweet_mins_before_match',
        'contains_will_win', 'contains_will_defeat',
       'contains_will_beat', 'contains_will_lose', 'contains_will_score',
       'contains_winner', 'contains_predict', 'contains_favorite',
       'contains_should', 'contains_win', 'contains_champion',
       'contains_victor', 'contains_upper_hand', 'contains_who',
       'contains_advantage', 'contains_lost', 'contains_to_win',
       'contains_contend', 'contains_outclassed', 'contains_defeat',
       'contains_with_win', 'contains_bat_first', 'contains_quotes',
       'contains_toss', 'contains_won_the_toss', 'contains_bowl_first',
       'contains_win_by', 'polarity', 'subjectivity']]
        final_x = final_x.fillna(0)

        return final_x



