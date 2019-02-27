import pandas as pd
import numpy as np
df = pd.read_csv("C:\\Users\\Yash\\AppData\\Local\\Programs\\Python\\Python36-32\\Machine Learning\\IPL\\deliveries.csv")
df1 = pd.read_csv("C:\\Users\\Yash\\AppData\\Local\\Programs\\Python\\Python36-32\\Machine Learning\\IPL\\matches.csv")
df = pd.merge(df, df1[["match_id", "season"]], on = "match_id")
df = df[(df["is_super_over"] != 1)]
df["wicket"] = df["dismissal_kind"].notnull().astype(int)
df["score"] = df.groupby(["match_id", "inning"]).total_runs.agg("cumsum")
df["wickets"] = df.groupby(["match_id", "inning"]).wicket.agg("cumsum")
res = df.groupby(by = (["season", "batting_team"]))["wicket"].apply(lambda x: x.sum()).reset_index().sort_values(by = ["season", "wicket"], ascending = False)
print(res)
