import pandas as pd
import numpy as np
df = pd.read_csv("C:\\Users\\Yash\\AppData\\Local\\Programs\\Python\\Python36-32\\Machine Learning\\IPL\\deliveries.csv")
df = df[(df["is_super_over"] != 1)]
g1 = df[["match_id", "batsman"]]
g2 = df[["match_id", "bowler"]]
g1 = g1.append(g2)
g1 = g1.fillna("zzzzzzzz")
g1[["bowler", "batsman"]] = np.sort(g1[["bowler", "batsman"]])
g1 = g1.drop(["batsman"], axis = 1)
g1["runs"] = 0
x = g1.groupby(["match_id", "bowler"])["runs"].agg("sum")
df_players = pd.DataFrame(data = {"match_id": x.index.get_level_values(0), "players": x.index.get_level_values(1)})
#df_players = df_players[df_players.match_id == 1]

b = df.groupby(["match_id", "batsman"])["batsman_runs"].sum()
df1 = pd.DataFrame(data = {"match_id":b.index.get_level_values(0), "players":b.index.get_level_values(1), "runs_scored":b.values})
df_players = pd.merge(df_players, df1, on=["match_id", "players"], how = "outer")

df["total_runs"] = df["total_runs"] - df["extra_runs"] + df["wide_runs"]
d1 = df.groupby(["match_id", "bowler"])["total_runs"].agg("sum")
df2= pd.DataFrame(data = {"match_id":d1.index.get_level_values(0), "players":d1.index.get_level_values(1), "runs_conceded":d1.values})
df_players = pd.merge(df_players, df2, on=["match_id", "players"], how = "outer")

df = df[(df["dismissal_kind"] != "run out") & (df["dismissal_kind"] != "obstructing the field") & (df["dismissal_kind"] != "retired hurt")]
d2 = df.groupby(["match_id", "bowler"])["player_dismissed"].agg("count")
df2 = pd.DataFrame(data = {"match_id":d2.index.get_level_values(0), "players":d2.index.get_level_values(1), "wickets":d2.values})
df_players = pd.merge(df_players, df2, on=["match_id", "players"], how = "outer")
df_players.fillna(0, inplace = True)
df_players
