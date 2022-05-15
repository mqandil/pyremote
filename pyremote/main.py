from pyremote.interest_index_scoring import MLBLiveData as mlblive
import webbrowser
import time
from IPython.display import display



if __name__ == '__main__':
    
    # while True:
    mlblivedata = mlblive()
    
    scoring_index_df = mlblivedata.get_interest_index_df()
    optimal_ii_link = scoring_index_df.iloc[0, 0]

    # display(mlblivedata.get_interest_index_df())
    # display(mlblivedata.get_ii_calculations())

    display(mlblivedata.get_live_situation_df())
        # time.sleep(120)
        
    
    webbrowser.get('safari').open(optimal_ii_link, new=0)