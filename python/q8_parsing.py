# The football.csv file contains the results from the English 
# Premier League. The columns labeled 'Goals' and 'Goals Allowed'
# contain the total number of goals scored for and against each 
# team in that season (so Arsenal scored 79 goals against opponents,
# and had 36 goals scored against them). Write a program to read 
# the file, then print the name of the team with the smallest
# difference in 'for' and 'against' goals.

import pandas as pd

football_df = pd.read_csv('football.csv')
football_df['Goal Difference'] = abs(football_df['Goals'] - football_df['Goals Allowed'])


# print football_df
# print
# print
# print
smallest_diff = football_df['Team'][football_df['Goal Difference'].idxmin()]

print '%s had the smallest difference between Goals and Goals Allowed, with a difference of %s goal(s).' % (smallest_diff, football_df['Goal Difference'].min())

