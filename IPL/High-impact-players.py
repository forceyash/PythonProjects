import pandas as pd
import numpy as np
df = pd.read_csv("C:\\Users\\yash.a.mishra\\AppData\\Local\\Programs\\Python\\Python37\\Machine Learning\\Pandas\\ipl\\deliveries.csv")
df_matches = pd.read_csv("C:\\Users\\yash.a.mishra\\AppData\\Local\\Programs\\Python\\Python37\\Machine Learning\\Pandas\\ipl\\matches.csv")

df = pd.merge(df, df_matches[["match_id", "season"]], on="match_id")
#print(df)

df = df[(df["is_super_over"] != 1)] #eliminate super overs
g1 = df[["match_id", "season", "batsman"]] #all batsmans in a match
g2 = df[["match_id", "season", "bowler"]] #all bowlers in a match
g1 = g1.append(g2)
g1 = g1.fillna("zzzzzzzz")
g1[["bowler", "batsman"]] = np.sort(g1[["bowler", "batsman"]])
g1 = g1.drop(["batsman"], axis = 1)
g1["runs"] = 0
x = g1.groupby(["match_id", "season", "bowler"])["runs"].agg("sum")

#all player played in a match
df_players = pd.DataFrame(data = {"match_id": x.index.get_level_values(0), "season": x.index.get_level_values(1), "players": x.index.get_level_values(2)})
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
df_players["points"] = (df_players["runs_scored"]/30 + df_players["wickets"])
print(df_players.nlargest(20, "points"))
print(df_players.groupby(["season", "players"])["points", "wickets", "runs_scored"].agg("sum").nlargest(20, "points"))
print(df_players.groupby(["players"])["points", "wickets", "runs_scored"].agg("sum").nlargest(20, "points"))
