import pandas as pd
import numpy as np

df = pd.read_csv("C:\\Users\\Yash\\AppData\\Local\\Programs\\Python\\Python36-32\\Machine Learning\\IPL\\deliveries.csv")
df = df[(df["is_super_over"] != 1)]
df["pri_key"] = df["match_id"].astype(str) + "-" + df["inning"].astype(str)
openners = df[(df["over"] == 1) & (df["ball"] == 1)]
openners = openners[["pri_key", "batsman", "non_striker"]]
openners = openners.rename(columns = {"batsman":"batter1", "non_striker":"batter2"})
df = pd.merge(df, openners, on="pri_key")
df = df[["batsman", "non_striker", "batter1", "batter2", "batsman_runs"]]
df = df[((df["batsman"] == df["batter1"]) | (df["batsman"] == df["batter2"]))
        & ((df["non_striker"] == df["batter1"]) | (df["non_striker"] == df["batter2"]))]

#df[['batsman', 'non_striker']] = df[['batsman', 'non_striker']].apply(sort, axis=1)
df[['batsman', 'non_striker']] = np.sort(df[['batsman', 'non_striker']],1)
print(df.groupby(['batsman', 'non_striker']).batsman_runs.sum().nlargest(10))
#df["batsman"] = df["batter1"]
#df["non-striker"] = df["batter2"]
#df["pairs"] = df["batsman"] + "-" + df["non_striker"]
#df1 = df.groupby(["batsman" , "non_striker"], group_keys = False)["batsman_runs"].agg("sum")
#df1.nlargest(10)
