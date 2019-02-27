import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("C:\\Users\\Yash\\AppData\\Local\\Programs\\Python\\Python36-32\\Machine Learning\\IPL\\deliveries.csv")
df_matches = pd.read_csv("C:\\Users\\Yash\\AppData\\Local\\Programs\\Python\\Python36-32\\Machine Learning\\IPL\\matches.csv")
df = pd.merge(df, df_matches[["match_id", "season"]], on="match_id")
df = df[(df["is_super_over"] != 1)]
player = input("enter a player name: ")
df = df[df.batsman == player]
df = df[["match_id", "season", "batsman", "batsman_runs", "player_dismissed"]]
x = df[df.player_dismissed == player]
balls_played = df.groupby(["match_id", "season", "batsman"])["batsman_runs"].agg("count")
runs_scored = df.groupby(["match_id","season", "batsman"])["batsman_runs"].agg("sum")
dismissed = x.groupby(["match_id", "season", "batsman"])["player_dismissed"].agg("count")
#balls_played
df1 = pd.DataFrame(data = {"match_id": balls_played.index.get_level_values(0), "balls": balls_played.values})
#runs_scored
df2 = pd.DataFrame(data = {"match_id": runs_scored.index.get_level_values(0), "Runs": runs_scored.values})
#dismissed
df3 = pd.DataFrame(data = {"match_id": dismissed.index.get_level_values(0), "out": dismissed.values})

player_data = pd.merge(df2, df1, on="match_id", how="outer")
player_data = pd.merge(player_data, df3, on="match_id", how = "outer")
player_data.fillna(0, inplace = True)

player_data["Carrer_Runs"] = player_data.Runs.cumsum()
player_data["Carrer_Balls"] = player_data.balls.cumsum()
player_data["dismissed"] = player_data.out.cumsum()
player_data["average"] = player_data["Carrer_Runs"]/player_data["dismissed"]
player_data["strike_rate"] = (player_data["Carrer_Runs"]/player_data["Carrer_Balls"])*100
player_data["match_no"] = np.arange(len(player_data))

my_plot = player_data.plot.line(x = "match_no", y = ["average", "strike_rate"])
plt.show()
#print(player_data)
