#Most successful bowler againist a batsman

import pandas as pd
import numpy as np

df = pd.read_csv("C:\\Users\\yash.a.mishra\\AppData\\Local\\Programs\\Python\\Python37\\Machine Learning\\Pandas\\ipl\\deliveries.csv")
batter = input("Name the batsman: ")
df = df[df.batsman == batter]
x = df.groupby("bowler")["batsman_runs"].agg({"Runs": "sum", "Balls":"count", "Strike_Rate":"mean"})
df = df[(df.player_dismissed == batter) & (df.dismissal_kind != "run out") & (df.dismissal_kind != "retired hurt")]
n = df.groupby("bowler")["player_dismissed"].agg({"Wickets": "count"})
x["Strike_Rate"] = x["Strike_Rate"]*100
x = pd.merge(x, n, on = "bowler", how = "outer")
x.fillna(0, inplace = True)
#print(x.nlargest(10, "Wickets").nsmallest(10, "Runs"))
#print(x.nlargest(10, "Wickets"))
print(x.nlargest(10, "Wickets").nsmallest(10, "Strike_Rate"))
