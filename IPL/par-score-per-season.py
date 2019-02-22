import pandas as pd
import numpy as np
df = pd.read_csv("C:\\Users\\Yash\\AppData\\Local\\Programs\\Python\\Python36-32\\Machine Learning\\IPL\\deliveries.csv")
df1 = pd.read_csv("C:\\Users\\Yash\\AppData\\Local\\Programs\\Python\\Python36-32\\Machine Learning\\IPL\\matches.csv")
df = pd.merge(df, df1[["match_id", "season"]], on = "match_id")
df = df[(df["is_super_over"] != 1)]
def func(x):
    a = x.total_runs.sum()/(x.match_id.nunique()*2)
    b = x.total_runs.where(x.inning == 1).sum()/(x.match_id.nunique())
    c = x.total_runs.where(x.inning == 2).sum()/(x.match_id.nunique())
    res = pd.DataFrame(data = {"Match":a, "1st innings":b, "2nd innings":c}, index = [1])
    return res
result = df.groupby("season")["inning", "total_runs", "match_id"].apply(lambda x: func(x))
print(result)
