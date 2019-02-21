import pandas as pd
import numpy as np

df_deliv = pd.read_csv("deliveries.csv")
df_match = pd.read_csv("matches.csv")
df_deliv = df_deliv[["match_id", "batting_team", "batsman", "batsman_runs"]]
df_deliv = pd.merge(df_deliv, df_match[["match_id", "winner"]], on = "match_id")
df_deliv = df_deliv.drop(df_deliv[df_deliv.batsman_runs == 0].index)
df_deliv = df_deliv[df_deliv["batting_team"] == df_deliv["winner"]]
df_group = pd.DataFrame(index = df_deliv["batsman"].unique(), columns=["runs"])
df_group.fillna(0, axis=0, inplace = True)
i = 0
x = len(df_deliv)

while(i < x):
    runs = df_deliv.iloc[i]["batsman_runs"]
    batter = df_deliv.iloc[i]["batsman"]
    p = df_group.iloc[df_group.index.get_loc(batter)][0] + np.int64(runs)
    df_group.iat[df_group.index.get_loc(batter),0] = p
    i=i+1
print(df_group.nlargest(10,"runs"))
