#Batsman pefromning against each team

import pandas as pd
import numpy as np

df = pd.read_csv("C:\\Users\\yash.a.mishra\\AppData\\Local\\Programs\\Python\\Python37\\Machine Learning\\Pandas\\ipl\\deliveries.csv")
#batter = input("Name the batsman: ")
#Highest run getter against a particular side
print(df.groupby(["batsman", "bowling_team"])["batsman_runs"].agg("sum").nlargest(10))
#Highest run getters against each side
x = df.groupby(["bowling_team", "batsman"])["batsman_runs"].agg("sum")
print(x.groupby(level = 0).nlargest(1).reset_index(level=0, drop = True))
