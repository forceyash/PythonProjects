import pandas as pd
import numpy as np

df = pd.read_csv("C:\\Users\\Yash\\AppData\\Local\\Programs\\Python\\Python36-32\\Machine Learning\\IPL\\deliveries.csv")
df = df[["batsman", "batsman_runs"]]
df = df[df["batsman_runs"]!=0]
result = pd.DataFrame(index = df["batsman"].unique(), columns=["runs without six"])
result.fillna(0, axis = 0, inplace = True)

i = 0
Len_of_df = len(df)
while(i < Len_of_df):
    runs = df.iloc[i]["batsman_runs"]
    batter = df.iloc[i]["batsman"]
    if(runs == 6):
        result.iat[result.index.get_loc(batter),0] = -1

    else:
        if(result.iloc[result.index.get_loc(batter)][0] != -1):
            p = result.iloc[result.index.get_loc(batter)][0] + np.int64(runs)
            result.iat[result.index.get_loc(batter),0] = p
    i=i+1
result = result[result["runs without six"]!=-1]
print(result.nlargest(10, "runs without six"))
