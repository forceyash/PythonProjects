import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

deliveries = pd.read_csv("C:\\Users\\Yash\\AppData\\Local\\Programs\\Python\\Python36-32\\Machine Learning\\IPL\\deliveries.csv")

Runs_given = deliveries.groupby("bowler").total_runs.agg({"Runs":"sum", "Balls":"count"})
deliveries = deliveries[(deliveries["dismissal_kind"] != "run out") & (deliveries["dismissal_kind"] != "obstructing the field") & (deliveries["dismissal_kind"] != "retired hurt")]
bowlers = deliveries.groupby("bowler")["player_dismissed"].agg({"wickets":"count"})

bowlers = pd.merge(Runs_given, bowlers, how = "outer", left_index = True, right_index = True)
bowlers["strike_rate"] = bowlers.Balls/bowlers.wickets
bowlers["Average"] = bowlers.Runs/bowlers.wickets
bowlers.nlargest(30,"wickets").nsmallest(30, "strike_rate")
