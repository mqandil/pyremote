import math

# Adjustement for overweighted late-inning blowouts
def leverage_qualifier_index(inning, run_diff):
    if inning <= 4:
        if run_diff <= 3:
            leverage_qualifier = (4-run_diff)
            return leverage_qualifier
        else:
            return 0
    elif inning >= 7:
        if run_diff >= 4 and run_diff <= 9:
            leverage_qualifier = -run_diff*(.25*inning)
            return leverage_qualifier
        else:
            return 1
    else:
        return 0


# Multiplier for opportunity for lead changes (if top of inning and away loosing or bottom and winning)
def lead_change_opp(home_run_diff, inning):

    inning_location = inning.split()[0]

    if home_run_diff == 0:
        return 1
    elif home_run_diff < 0 and (inning_location == 'MID' or inning_location == 'BOT'):
        return 1
    elif home_run_diff > 0 and (inning_location == 'END' or inning_location == 'TOP'):
        return 1
    else:
        return 0

def inning_score_index(inning):
    inning_score = 0.6489*math.e**(0.1954*inning)
    return inning_score

def run_diff_score_index(run_diff):
    if run_diff < 5:
        run_diff_score = -0.125*run_diff**4+0.9167*run_diff**3-1.875*run_diff**2+0.0833*run_diff+10
        return run_diff_score
    elif run_diff >= 5:
        run_diff_score = 0.00009*run_diff**4-0.0066*run_diff**3+0.1697*run_diff**2-1.5997*run_diff+6.131
        return run_diff_score

# Final Equation
def get_interest_index(runners_score, inning_score, outs_score, run_diff_score, lead_change_opp_score, leverage_qualifier):
    interest_index = (runners_score+run_diff_score)*(1+0.75*lead_change_opp_score)*outs_score*inning_score+leverage_qualifier
    return interest_index