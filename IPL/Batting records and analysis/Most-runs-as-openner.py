#most runs as opener

import pandas as pd
import numpy as np

df = pd.read_csv("C:\\Users\\yash.a.mishra\\AppData\\Local\\Programs\\Python\\Python37\\Machine Learning\\Pandas\\ipl\\deliveries.csv")
df = df[(df["is_super_over"] != 1)]
df["pri_key"] = df["match_id"].astype(str) + "-" + df["inning"].astype(str)
openners = df[(df["over"] == 1) & (df["ball"] == 1)]
openners = openners[["pri_key", "batsman", "non_striker"]]
openners = openners.rename(columns = {"batsman":"batter1", "non_striker":"batter2"})
df = pd.merge(df, openners, on="pri_key")
df = df[["batsman", "batter1", "batter2", "batsman_runs"]]
df = df[(df["batsman"] == df["batter1"]) | (df["batsman"] == df["batter2"])]
df = df[df["batsman_runs"] >= 1]
print(df.groupby(["batsman"])["batsman_runs"].agg("sum").nlargest(10))
