import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time
start = time. time()

deliveries = pd.read_csv("C:\\Users\\Yash\\AppData\\Local\\Programs\\Python\\Python36-32\\Machine Learning\\IPL\\deliveries.csv")
#deliveries.drop_duplicates(["match_id", "batsman"]).groupby("batsman").match_id.agg("count").nlargest(30)
"""
x = deliveries[["match_id", "batsman"]].append(deliveries[["match_id", "bowler"]]).append(deliveries[["match_id", "fielder"]]).fillna("zzzzz")
x[["batsman", "bowler"]] = np.sort(x[["batsman", "bowler"]])
x[["batsman", "fielder"]] = np.sort(x[["batsman", "fielder"]])
x = x.drop(["bowler", "fielder"], axis =1)
x = x[x.batsman != "zzzzz"]
print(x.drop_duplicates(["match_id", "batsman"]).groupby("batsman").match_id.agg("count").nlargest(30))

"""

#----------------------------------------------slower-------------------------------------------------
def func1(x):
    batters = x.batsman.unique()
    bowlers = x.bowler.unique()
    fielder = x.fielder.unique()
    All = np.concatenate((batters, bowlers, fielder))
    All = pd.Series(np.array(All).tolist())
    All = All[~All.duplicated()]
    All = pd.DataFrame(data = {"Player": All})
    return All

mapper = deliveries.groupby('match_id')["batsman", "bowler", "fielder"].apply(lambda x: func1(x)).reset_index().drop(["level_1"], axis = 1).dropna()
print(mapper.groupby("Player").match_id.count().nlargest(30))
#"""
end = time. time()
print(end - start)
