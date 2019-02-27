import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

deliveries = pd.read_csv("C:\\Users\\Yash\\AppData\\Local\\Programs\\Python\\Python36-32\\Machine Learning\\IPL\\deliveries.csv")
deliveries_matches = pd.read_csv("C:\\Users\\Yash\\AppData\\Local\\Programs\\Python\\Python36-32\\Machine Learning\\IPL\\matches.csv")

batters = deliveries.groupby("batsman").batsman_runs.agg({"Runs":"sum"})
fielders = deliveries.groupby("fielder").fielder.agg({"dismmisal":"count"})
deliveries = deliveries[(deliveries["dismissal_kind"] != "run out") & (deliveries["dismissal_kind"] != "obstructing the field") & (deliveries["dismissal_kind"] != "retired hurt")]
bowlers = deliveries.groupby("bowler")["player_dismissed"].agg({"wickets":"count"})

players = pd.merge(batters, fielders, how = "outer", left_index = True, right_index = True)
players = pd.merge(players, bowlers, how = "outer", left_index = True, right_index = True)
players.nlargest(30, "dismmisal").nlargest(30,"wickets")
