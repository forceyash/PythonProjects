#Most-matches-at-venues

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv("C:\\Users\\yash.a.mishra\\AppData\\Local\\Programs\\Python\\Python37\\Machine Learning\\Pandas\\ipl\\matches.csv")
df["venue"] = np.where((df["venue"] == "Punjab Cricket Association IS Bindra Stadium, Mohali"), "Punjab Cricket Association Stadium, Mohali", df["venue"])
grounds = df["venue"].value_counts().reset_index().rename(columns = {"index": "venues", "venue": "Matches"})
city = df["city"].value_counts().reset_index().rename(columns = {"index": "city", "city": "matches"})
print(df[["city", "venue"]].groupby(["city"]).venue.nunique().reset_index().sort_values(by = "venue", ascending = False))

"""
grounds (top 10)
                                               venues  Matches
0                               M Chinnaswamy Stadium       66
1                                        Eden Gardens       61
2                                    Feroz Shah Kotla       60
3                                    Wankhede Stadium       57
4           Rajiv Gandhi International Stadium, Uppal       49
5                     MA Chidambaram Stadium, Chepauk       48
6          Punjab Cricket Association Stadium, Mohali       35
7                              Sawai Mansingh Stadium       33
8                          Subrata Roy Sahara Stadium       17
9                          Dr DY Patil Sports Academy       17
10            Maharashtra Cricket Association Stadium       15

----------------------------------------------------------------------
cities (top 10)

              city  matches
0           Mumbai       85
1        Bangalore       66
2          Kolkata       61
3            Delhi       60
4        Hyderabad       49
5          Chennai       48
6       Chandigarh       46
7           Jaipur       33
8             Pune       32
9           Durban       15
10       Centurion       12

----------------------------------------------------------------------
cities with more than 1 venues

              city  venues
1           Mumbai      3
2             Pune      2

"""
