from pyremote.datasources.parse_html import ParseHtml
import pandas as pd

def df_compiler():

    data_html = ParseHtml()

    # Get Data
    links = data_html.get_mlb_live_links()
    teams = data_html.get_team_matchups()
    scores = data_html.get_scores()
    innings = data_html.get_innings()
    runners = data_html.get_runners()
    outs = data_html.get_outs()

    # Get Home and Away Teams/Matchups
    home_teams = []
    away_teams = []
    i = 0
    for team in teams:
        if i%2 == 0:
            away_teams.append(team)
        elif i%2 != 0:
            home_teams.append(team)
        i+=1

    # Get Home and Away Scores
    home_scores = []
    away_scores = []
    i = 0
    for score in scores:
        if i%2 == 0:
            away_scores.append(score)
        elif i%2 != 0:
            home_scores.append(score)
        i+=1

    # Create Main DataFrame and Transpose
    live_data = pd.DataFrame(
        data=[
            links, 
            away_teams,
            away_scores, 
            home_teams, 
            home_scores, 
            innings
            ]
    )
    live_data = live_data.T

    # Rename Columns
    live_data = live_data.rename(columns={0: "link", 1: "away_team", 2: "away_score", 3: "home_team", 4: "home_score", 5: "inning"})

    # Remove Data where Final
    live_data = live_data[~live_data.inning.str.contains("Final", regex=False, na=False)]
    live_data = live_data[~live_data.inning.str.contains("ET", regex=False, na=False)]

    # Add Runners and Outs
    live_data['runners'] = runners
    live_data['outs'] = outs

    # Remove Games where inning is blank (games in warmup)
    live_data = live_data[live_data.inning != '']

    # Run Diff
    live_data['home_run_diff'] = live_data['home_score'].astype(int) - live_data['away_score'].astype(int)
    live_data['run_diff'] = abs(live_data['home_run_diff'])

    return live_data


if __name__ == '__main__':
    print(df_compiler())