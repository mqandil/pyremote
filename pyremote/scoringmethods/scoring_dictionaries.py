
# Total Bases + 1 (because games with no runners on base may still be worth watching)
runners_value_dict = {
    'No runners on base': 1,
    'Runner at 1st': 2,
    'Runner  at 1st': 2,
    'Runner at  1st': 2,
    'Runner  at 2nd': 3, 
    'Runner  at 3rd': 4, 
    'Runners  at 1st & 2nd': 5, 
    'Runners  at 1st & 3rd': 6, 
    'Runners  at 2nd & 3rd': 7, 
    'Base loaded': 9
}

outs_value_dict = {
    '0 Out': 1.5,
    '1 Out': 1.5,
    '2 Outs': 1.5, 
    '3 Outs': 1, 
}
