#teams winning the toss and match too
import pandas as pd
import numpy as np
df = pd.read_csv("C:\\Users\\Yash\\AppData\\Local\\Programs\\Python\\Python36-32\\Machine Learning\\IPL\\matches.csv")
z = df.groupby("winner")["toss_winner", "winner"].apply(lambda x: np.where(x.toss_winner == x.winner, 1, 0).sum()).reset_index().rename(columns = {"winner":"team", 0:"toss wins"})
team1 = df.groupby("team1").match_id.count().reset_index().rename(columns = {"team1":"team", "match_id":"a"})
team2 = df.groupby("team2").match_id.count().reset_index().rename(columns = {"team2":"team", "match_id":"b"})
matches_played = pd.merge(team1, team2, on = "team")
matches_played["played"] = matches_played["a"] + matches_played["b"]
matches_played.drop(columns = ["a", "b"], inplace = True)
z = pd.merge(matches_played, z, on = "team")
z["win_pct"] = (z["toss wins"]/z["played"])*100
z.sort_values(by = ["played", "win_pct"], ascending=False)

#Analysis
#Among the teams that has played more than 100 IPL games (origional seven team)
#Luckiest Team:    Chennai Super Kings - 32.06%
#un-Luckiest Team: Kings XI Punjab     - 18.91%

#Among all teams in IPL
#Luckiest Team:    Gujarat Lions - 33.33%
#un-Luckiest Team: Pune Warriors - 6.52%
