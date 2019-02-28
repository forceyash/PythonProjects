#Teams performace at venues
#                                                                                         Wins   Matches  win-percentage
#best team at home ground:  Rajasthan Royals - Sawai Mansingh Stadium                     24.0      33       72.73
#worst team at home ground: Deccan Chargers - Rajiv Gandhi International Stadium, Uppal    3.0      18       16.67
#best visiting team:         Mumbai Indians -       Eden Gardens                           9.0      11       81.82
#                            Mumbai Indians -    M Chinnaswamy Stadium                     8.0      10       80.00


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv("C:\\Users\\yash.a.mishra\\AppData\\Local\\Programs\\Python\\Python37\\Machine Learning\\Pandas\\ipl\\matches.csv")
def func(x):
    return x.sort_values(by = "matches", ascending=False)#.nlargest(3, "matches")

z = df.groupby(["winner", "venue"])["match_id"].count().reset_index().rename(columns = {"winner":"team", "match_id":"matches"})
z = z.groupby("team").apply(lambda x: func(x)).drop(["team"], axis = 1).reset_index().drop(columns = ["level_1"])

def func1(x):
    teams = np.concatenate((x.team1.values, x.team2.values), axis = 0)
    return pd.Series(teams).value_counts().reset_index()

y = df.groupby(["venue"])["match_id", "team1", "team2"].apply(lambda x: func1(x)).reset_index().drop(columns = ["level_1"]).rename(columns = {"index":"team", 0:"played"})
y = y.groupby("team")["venue", "played"].apply(lambda x: x.sort_values(by = "played", ascending=False)).reset_index().drop(columns = ["level_1"])


mgrd_df = pd.merge(z, y, on = ["team", "venue"], how = "outer")
mgrd_df.fillna(0, inplace = True)
mgrd_df["win_pct"] = np.round(mgrd_df["matches"]/mgrd_df["played"]*100, 2)
mgrd_df = mgrd_df.sort_values(by = ["team", "matches"], ascending = [True, False])
#mgrd_df.to_csv("temp.csv",  sep=',', encoding='utf-8')
print(mgrd_df[mgrd_df["played"] > 7].sort_values(by = "win_pct", ascending = False))
