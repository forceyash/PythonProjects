#most runs as opener

import pandas as pd
import numpy as np

df = pd.read_csv("deliveries.csv")
df["openner"] = 0
i = 0
df_len = len(df)
batter1 = ""
batter2 = ""

while(i<df_len):
    if (df.loc[i,"over"] == 1) & (df.loc[i, "ball"] == 1) & (df.loc[i, "is_super_over"]!=1):
        batter1 =  df.loc[i,"batsman"]
        batter2 =  df.loc[i, "non_striker"]

    if ((df.loc[i,"batsman"] == batter1) | (df.loc[i,"batsman"] == batter2)):
        df.iat[i,df.columns.get_loc("openner")] = True
    else:
        df.iat[i,df.columns.get_loc("openner")] = False
    i=i+1

df = df[df["openner"] == 1]
df = df[df["batsman_runs"] >= 1]
df = df[["batsman", "batsman_runs"]]

runsAsOpener = pd.DataFrame(columns = ["batsman", "runs"])
runsAsOpener["batsman"] = df["batsman"].unique()
runsAsOpener["runs"] = 0

#print(runsAsOpener)
#print(df[df["batsman"] == ""].sum()[1])
i = 0
df_len = len(runsAsOpener)
while(i < df_len):
    batter = runsAsOpener.loc[i, "batsman"]
    runsAsOpener.iat[i, 1] = df[df["batsman"] == batter].sum()[1]
    i=i+1
#df["opener"] = (df["over"] == 1) & (df["ball"] == 1) & (df["is_super_over"]!=1)
#df.fillna(0, axis=0, inplace = True)
#openers = openers[["match_id", "batting_team", "batsman", "non_striker"]]
#df["opener"] = df[(df["batsman"] and df["match_id"]).isin(openers["batsman"] and openers["match_id"])]
#print(runsAsOpener.loc[[runsAsOpener["runs"].idxmax()]])
print(runsAsOpener.nlargest(10, "runs"))
