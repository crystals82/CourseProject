import pandas as pd
from schedule_transform_utils import schedule_transfrom_utilities
class transform_schedule:
    def __init__(self):
        self.status = 'on'

    def make_transformations(df):
        df['clean_datetime_of_match_ist'] = pd.to_datetime(df['Date'] + ' ' + df['Time (IST)'])
        df['clean_datetime_of_match_ist'] = df['clean_datetime_of_match_ist'].dt.tz_localize('Asia/Kolkata')
        df['clean_datetime_of_match_est'] = df['clean_datetime_of_match_ist'].dt.tz_convert('America/New_York')
        df['clean_datetime_of_match_utc'] = df['clean_datetime_of_match_est'].dt.tz_convert(None)
        df['Teams'] = df['Teams'].str.lower()
        df['team_1'] = df['Teams'].str.split(' vs ').str[0]
        df['team_2'] = df['Teams'].str.split(' vs ').str[1]
        df['winner_of_match'] = df['Result'].str[:3]
        df['winner_of_match'] = df['winner_of_match'].str.strip()
        df['result_by_wickets'] = df['Result'].str.contains('wickets')
        df['result_by_runs'] = df['Result'].str.contains('runs')
        df['result_quantity'] = df.Result.str.extract('(\d+)')
        df['winner_of_match_expanded'] = df.apply(schedule_transfrom_utilities.assign_team_from_alias, axis = 1)
        df['team_1_alias'] = df.apply(schedule_transfrom_utilities.assign_team_1_alias, axis = 1)
        df['team_2_alias'] = df.apply(schedule_transfrom_utilities.assign_team_2_alias, axis = 1)
        df['hashtag1'] = df['team_1_alias'] + 'v' + df['team_2_alias']
        df['hashtag2'] = df['team_2_alias'] + 'v' + df['team_1_alias']
        return df
