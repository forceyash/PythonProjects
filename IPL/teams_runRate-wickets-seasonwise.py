import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

deliveries = pd.read_csv("C:\\Users\\Yash\\AppData\\Local\\Programs\\Python\\Python36-32\\Machine Learning\\IPL\\deliveries.csv")
matches = pd.read_csv("C:\\Users\\Yash\\AppData\\Local\\Programs\\Python\\Python36-32\\Machine Learning\\IPL\\matches.csv")
deliveries = pd.merge(deliveries, matches[["match_id", "season"]], on="match_id")
deliveries = deliveries[(deliveries.is_super_over == 0)]
deliveries = deliveries[["match_id", "batting_team" ,"season", "inning", "over", "ball", "total_runs", "player_dismissed"]]
powerplay = deliveries[(deliveries.over <= 6)]
middleovers = deliveries[(deliveries.over >= 7) & (deliveries.over <= 14)]
slogovers = deliveries[(deliveries.over >= 15)]
#m = powerplay.groupby(["season", "batting_team"])["total_runs", "match_id"].apply(lambda x: pd.DataFrame(data = {"Runs": x.total_runs.sum(), "Matches":x.match_id.nunique(), "Run_rate": x.total_runs.sum()/(x.match_id.nunique()*6)}, index = np.arange(1))).nlargest(10, "Run_rate")#.reset_index().drop("level_2", axis = 1)
#a = powerplay.groupby(["season", "batting_team"])["total_runs", "match_id"].apply(lambda x: x.total_runs.sum()/(x.match_id.nunique()*6)).reset_index(name = 'powerplay')
a = powerplay.groupby(["season", "batting_team"])["total_runs", "match_id", "player_dismissed"].apply(lambda x: pd.DataFrame(data = {"Runrate(1-6)" : x.total_runs.sum()/(x.match_id.nunique()*6), "wickets(1-6)":np.around(x.player_dismissed.dropna().count()/(x.match_id.nunique()), decimals = 2)}, index = np.arange(1))).reset_index().drop("level_2", axis = 1)
b = middleovers.groupby(["season", "batting_team"])["total_runs", "match_id", "player_dismissed"].apply(lambda x: pd.DataFrame(data = {"Runrate(7-14)" : x.total_runs.sum()/(x.match_id.nunique()*8), "wickets(7-14)":np.around(x.player_dismissed.dropna().count()/(x.match_id.nunique()), decimals = 2)}, index = np.arange(1))).reset_index().drop("level_2", axis = 1)
c = slogovers.groupby(["season", "batting_team"])["total_runs", "match_id", "player_dismissed"].apply(lambda x: pd.DataFrame(data = {"Runrate(15-20)" : x.total_runs.sum()/(x.match_id.nunique()*6), "wickets(15-20)":np.around(x.player_dismissed.dropna().count()/(x.match_id.nunique()), decimals = 2)}, index = np.arange(1))).reset_index().drop("level_2", axis = 1)
report = pd.merge(a, b, on = (["season", "batting_team"]))
report = pd.merge(report, c, on = (["season", "batting_team"]))
report.groupby("season").apply(lambda x: x.sort_values(by = "wickets(7-14)", ascending=False)[:5])
