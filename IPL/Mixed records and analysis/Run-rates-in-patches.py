import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

deliveries = pd.read_csv("C:\\Users\\yash.a.mishra\\AppData\\Local\\Programs\\Python\\Python37\\Machine Learning\\Pandas\\ipl\\deliveries.csv")
matches = pd.read_csv("C:\\Users\\yash.a.mishra\\AppData\\Local\\Programs\\Python\\Python37\\Machine Learning\\Pandas\\ipl\\matches.csv")
deliveries = pd.merge(deliveries, matches[["match_id", "season"]], on="match_id")
deliveries = deliveries[(deliveries.is_super_over == 0)]
deliveries = deliveries[["match_id", "batting_team" ,"season", "inning", "over", "ball", "total_runs"]]
powerplay = deliveries[(deliveries.over <= 6)]
middleovers = deliveries[(deliveries.over >= 7) & (deliveries.over <= 14)]
slogovers = deliveries[(deliveries.over >= 15)]
#m = powerplay.groupby(["season", "batting_team"])["total_runs", "match_id"].apply(lambda x: pd.DataFrame(data = {"Runs": x.total_runs.sum(), "Matches":x.match_id.nunique(), "Run_rate": x.total_runs.sum()/(x.match_id.nunique()*6)}, index = np.arange(1))).nlargest(10, "Run_rate")#.reset_index().drop("level_2", axis = 1)
a = powerplay.groupby(["season", "batting_team"])["total_runs", "match_id"].apply(lambda x: x.total_runs.sum()/(x.match_id.nunique()*6)).reset_index(name = 'powerplay')#.rename(columns = {'level_2':'Run_rate'})
b = middleovers.groupby(["season", "batting_team"])["total_runs", "match_id"].apply(lambda x: x.total_runs.sum()/(x.match_id.nunique()*8)).reset_index(name = 'middleovers')
c = slogovers.groupby(["season", "batting_team"])["total_runs", "match_id"].apply(lambda x: x.total_runs.sum()/(x.match_id.nunique()*6)).reset_index(name = 'slogovers')
report = pd.merge(a, b, on = (["season", "batting_team"]))
report = pd.merge(report, c, on = (["season", "batting_team"]))
print(report)
