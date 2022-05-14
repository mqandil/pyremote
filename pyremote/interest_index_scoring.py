from scoringmethods.scoring_dictionaries import runners_value_dict, outs_value_dict
from scoringmethods.scoring_functions import run_diff_score_index, lead_change_opp, leverage_qualifier_index, get_interest_index, inning_score_index
from datahelpers.data_compiler import df_compiler

class MLBLiveData():
    def __init__(self):
        self.live_data = df_compiler()
        # Adding Scores
        self.live_data['runners_score'] = self.live_data['runners'].map(runners_value_dict)
        self.live_data['inning_score'] = self.live_data.apply(
            lambda row: inning_score_index(int(row['inning'].split()[1])), axis=1
        )
        self.live_data['outs_score'] = self.live_data['outs'].map(outs_value_dict)
        self.live_data['run_diff_score'] = self.live_data.apply(
            lambda row: run_diff_score_index(row['run_diff']), axis=1
        )
        self.live_data['lead_change_opp_score'] = self.live_data.apply(
            lambda row: lead_change_opp(row['home_run_diff'], row['inning']), axis=1
        )
        self.live_data['leverage_qualifier'] = self.live_data.apply(
            lambda row: leverage_qualifier_index(int(row['inning'].split()[1]), row['run_diff']), axis=1
        )
        self.live_data['interest_index'] = self.live_data.apply(
            lambda row: get_interest_index(row['runners_score'], row['inning_score'], row['outs_score'], row['run_diff_score'], row['lead_change_opp_score'], row['leverage_qualifier']), axis=1
        )

    def get_live_situation_df(self):
        return self.live_data[['away_team', 'away_score', 'home_team', 'home_score', 'inning', 'runners', 'outs', 'home_run_diff', 'interest_index']].sort_values(by = 'interest_index', ascending=False)

    def get_interest_index_df(self):
        return self.live_data[['link', 'interest_index']].sort_values(by = 'interest_index', ascending=False)

    def get_ii_calculations(self):
        return self.live_data[['runners_score', 'inning_score', 'outs_score', 'run_diff_score', 'lead_change_opp_score', 'leverage_qualifier', 'interest_index']].sort_values(by = 'interest_index', ascending=False)

if __name__ == '__main__':
    LiveData = MLBLiveData()
    # print(LiveData.get_live_situation_df())
    # LiveData.get_live_situation_df