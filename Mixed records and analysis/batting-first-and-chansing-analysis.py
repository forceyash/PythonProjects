import pandas as pd
import numpy as np
df = pd.read_csv("C:\\Users\\Yash\\AppData\\Local\\Programs\\Python\\Python36-32\\Machine Learning\\IPL\\matches.csv")
def func(x):
    a = x.win_by_runs.where(x.win_by_runs != 0).count()
    b = x.win_by_wickets.where(x.win_by_wickets != 0).count()
    res = pd.DataFrame(data = {"Batting first":a, "chasing":b}, index = [1])
    return res
result = df.groupby("season")["win_by_runs", "win_by_wickets", "match_id"].apply(lambda x: func(x)).reset_index().drop(columns = "level_1", axis =1)
result = result.append(pd.DataFrame(data = {"season": "total", "Batting first": result["Batting first"].sum(), "chasing": result["chasing"].sum()}, index = [1]))
print(result)
