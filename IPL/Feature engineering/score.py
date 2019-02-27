import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

deliveries = pd.read_csv("C:\\Users\\yash.a.mishra\\AppData\\Local\\Programs\\Python\\Python37\\Machine Learning\\Pandas\\ipl\\deliveries.csv")
matches = pd.read_csv("C:\\Users\\yash.a.mishra\\AppData\\Local\\Programs\\Python\\Python37\\Machine Learning\\Pandas\\ipl\\matches.csv")
deliveries = pd.merge(deliveries, matches[["match_id", "season"]], on="match_id")
deliveries = deliveries[(deliveries.is_super_over == 0)]
deliveries = deliveries[["match_id", "batting_team" ,"season", "inning", "over", "ball", "total_runs", "player_dismissed"]]
score = deliveries.groupby(["match_id", "inning"]).match_id.apply(lambda x: pd.DataFrame(data = {"match_id": x.match_id, "inning": x.inning,  "Score": x["total_runs"].cumsum(), "Wickets":(x["player_dismissed"].notnull()).astype("int").cumsum()})).reset_index()
deliveries = pd.merge(deliveries, score[["match_id", "inning", "Score", "Wickets"]], on=(["match_id", "inning"]), how = "inner")
print(deliveries)
#train_data = deliveries[(deliveries.season != 2016) & (deliveries.season != 2017)]
#test_data = deliveries[(deliveries.season == 2016) | (deliveries.season == 2017)]
