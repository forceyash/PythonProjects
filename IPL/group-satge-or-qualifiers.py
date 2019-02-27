#identifying groupsatge matches and qualifiers
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("C:\\Users\\yash.a.mishra\\AppData\\Local\\Programs\\Python\\Python37\\Machine Learning\\Pandas\\ipl\\matches.csv")
def func(x):
    res = pd.DataFrame(data = {"match_id":np.sort(x)})
    res["stage"] = np.where(res["match_id"].isin(res["match_id"][:-4]), "Group stage", "Qualifier")
    res.loc[len(res)-1,"stage"] = "Final"
    res.loc[len(res)-2,"stage"] = "Eliminator 2"
    res.loc[len(res)-3,"stage"] = "Eliminator 1"
    return res

df1 = df.groupby("season")["match_id"].apply(lambda x: func(x)).reset_index().drop(columns = "level_1")
df = pd.merge(df, df1[["match_id", "stage"]], on = "match_id")

#print(df[["season", "match_id", "stage"]])
