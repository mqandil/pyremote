from pyremote.interest_index_scoring import MLBLiveData as mlblive
import webbrowser
from pyremote.datasources.request_timer import variable_timer
import time
from IPython.display import display

class OptimalLinkInfo():
    def __init__(self):
        self.mlblivedata = mlblive()

    def open_optimal_link(self):
        scoring_index_df = self.mlblivedata.get_interest_index_df().sort_values(by = 'interest_index', ascending=False)
        optimal_ii_link = scoring_index_df.iloc[0, 0]

        webbrowser.get('safari').open(optimal_ii_link)

    def get_optimal_link(self):
        scoring_index_df = self.mlblivedata.get_interest_index_df().sort_values(by = 'interest_index', ascending=False)
        optimal_ii_link = scoring_index_df.iloc[0, 0]
        return optimal_ii_link

    def get_inning(self):
        live_situation_df = self.mlblivedata.get_live_situation_df().sort_values(by = 'interest_index', ascending=False)
        inning = live_situation_df['inning'][0]
        inning_part = inning.split()[0]
        inning_int = inning.split()[1]
        return inning_part, inning_int

    def display_data(self):
        table = self.mlblivedata.get_live_situation_df()
        display(table)

def mlb_live_updater():
    
    last_link = ''
    last_link_inning_part = ''

    while True:
        print('Initializing...')
        new_link_info = OptimalLinkInfo()
        new_link = new_link_info.get_optimal_link()
        new_link_inning_part = new_link_info.get_inning()[0]
        new_link_info.display_data()

        if last_link == new_link:
            print('You are still watching the most interesting game!')
        
        elif last_link != new_link:
            if last_link_inning_part != new_link_inning_part:
                print('Another game is now more interesting!')
                new_link_info.open_optimal_link()

                last_link = new_link
                last_link_inning_part = new_link_inning_part
            else:
                print('The inning has not ended!')
        else:
            raise ValueError('Something went wrong! Please try again.')

        variable_timer()


mlb_live_updater()