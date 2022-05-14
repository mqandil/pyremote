from interest_index_scoring import MLBLiveData as mlblive
import webbrowser

mlblivedata = mlblive()
scoring_index_df = mlblivedata.get_interest_index_df()
optimal_ii_link = scoring_index_df.iloc[0, 0]

print(mlblivedata.get_interest_index_df())
print(mlblivedata.get_ii_calculations())
print(mlblivedata.get_live_situation_df())
# webbrowser.open(optimal_ii_link)

if __name__ == '__main__':
    pass