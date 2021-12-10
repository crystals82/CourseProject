import pandas as pd

class schedule_transfrom_utilities:
    def __init__(self):
        self.status = 'on'

    def assign_team_from_alias(df):
        if (df['winner_of_match'] == 'OMN'):
            return 'oman'
        elif (df['winner_of_match'] == 'SCO'):
            return 'scotland'
        elif (df['winner_of_match'] == 'IRE'):
            return 'ireland'
        elif (df['winner_of_match'] == 'BAN'):
            return 'bangladesh'
        elif (df['winner_of_match'] == 'SRI'):
            return 'sri lanka'
        elif (df['winner_of_match'] == 'NAM'):
            return 'namibia'
        elif (df['winner_of_match'] == 'SL'):
            return 'sri lanka'
        elif (df['winner_of_match'] == 'AUS'):
            return 'australia'
        elif (df['winner_of_match'] == 'ENG'):
            return 'england'
        elif (df['winner_of_match'] == 'PAK'):
            return 'pakistan'
        elif (df['winner_of_match'] == 'AGG'):
            return 'afghanistan'
        elif (df['winner_of_match'] == 'SA'):
            return 'south africa'
        elif (df['winner_of_match'] == 'WI'):
            return 'west indies'
        elif (df['winner_of_match'] == 'AFG'):
            return 'afghanistan'
        elif (df['winner_of_match'] == 'NZ'):
            return 'new zealand'
        elif (df['winner_of_match'] == 'IND'):
            return 'india'

    def assign_team_1_alias(df):
    
        if (df['team_1'] == 'oman'):
            return 'OMN'
        elif (df['team_1'] == 'scotland'):
            return 'SCO'
        elif (df['team_1'] == 'ireland'):
            return 'IRE'
        elif (df['team_1'] == 'bangladesh'):
            return 'BAN'
        elif (df['team_1'] == 'sri lanka'):
            return 'SL'
        elif (df['team_1'] == 'namibia'):
            return 'NAM'
        elif (df['team_1'] == 'australia'):
            return 'AUS'
        elif (df['team_1'] == 'england'):
            return 'ENG'
        elif (df['team_1'] == 'pakistan'):
            return 'PAK'
        elif (df['team_1'] == 'afghanistan'):
            return 'AFG'
        elif (df['team_1'] == 'south africa'):
            return 'SA'
        elif (df['team_1'] == 'west indies'):
            return 'WI'
        elif (df['team_1'] == 'zealand'):
            return 'NZ'
        elif (df['team_1'] == 'india'):
            return 'IND'
        elif (df['team_1'] == 'netherlands'):
            return 'NED'
        elif (df['team_1'] == 'papua new guinea'):
            return 'PNG'
        elif (df['team_1'] == 'new zealand'):
            return 'NZ'


    def assign_team_2_alias(df):
    
        if (df['team_2'] == 'oman'):
            return 'OMN'
        elif (df['team_2'] == 'scotland'):
            return 'SCO'
        elif (df['team_2'] == 'ireland'):
            return 'IRE'
        elif (df['team_2'] == 'bangladesh'):
            return 'BAN'
        elif (df['team_2'] == 'sri lanka'):
            return 'SL'
        elif (df['team_2'] == 'namibia'):
            return 'NAM'
        elif (df['team_2'] == 'australia'):
            return 'AUS'
        elif (df['team_2'] == 'england'):
            return 'ENG'
        elif (df['team_2'] == 'pakistan'):
            return 'PAK'
        elif (df['team_2'] == 'afghanistan'):
            return 'AFG'
        elif (df['team_2'] == 'south africa'):
            return 'SA'
        elif (df['team_2'] == 'west indies'):
            return 'WI'
        elif (df['team_2'] == 'zealand'):
            return 'NZ'
        elif (df['team_2'] == 'india'):
            return 'IND'
        elif (df['team_2'] == 'netherlands'):
            return 'NED'
        elif (df['team_2'] == 'papua new guinea'):
            return 'PNG'
        elif (df['team_2'] == 'new zealand'):
            return 'NZ'