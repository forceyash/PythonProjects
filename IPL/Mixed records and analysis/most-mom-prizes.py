#most man of the match awards

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv("C:\\Users\\yash.a.mishra\\AppData\\Local\\Programs\\Python\\Python37\\Machine Learning\\Pandas\\ipl\\matches.csv")
print(df.groupby("player_of_match").match_id.agg("count").reset_index().rename(columns = {"match_id":"mom"}).nlargest(20, "mom"))

#most man of the match awards in a season
print(df.groupby(["player_of_match", "season"]).match_id.agg("count").reset_index().rename(columns = {"match_id":"mom"}).nlargest(20, "mom"))
