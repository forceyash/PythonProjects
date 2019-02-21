import pandas as pd
df = pd.read_csv("C:\\Users\\Yash\\AppData\\Local\\Programs\\Python\\Python36-32\\Machine Learning\\IPL\\deliveries.csv")
df = df[(df["is_super_over"] != 1)]
df["total_runs"] = df["total_runs"] - df["extra_runs"] + df["wide_runs"]
d1 = df.groupby(["match_id", "bowler"])["total_runs"].agg("sum")
df1= pd.DataFrame(data = {"match_id":d1.index.get_level_values(0), "bowler":d1.index.get_level_values(1), "runs":d1.values})
df = df[(df["dismissal_kind"] != "run out") & (df["dismissal_kind"] != "obstructing the field") & (df["dismissal_kind"] != "retired hurt")]
d2 = df.groupby(["match_id", "bowler"])["player_dismissed"].agg("count")
df2 = pd.DataFrame(data = {"match_id":d2.index.get_level_values(0), "bowler":d2.index.get_level_values(1), "wickets":d2.values})
df3 = pd.merge(df1, df2, on = ["match_id", "bowler"])
df3.drop("match_id", axis = 1, inplace = True)
df3.sort_values(["runs"], inplace = True)#, "wickets"], ascending=[True, False])
df3.nlargest(10, "wickets")


b = df.groupby(["match_id", "batsman"])["batsman_runs"].sum()
df4 = pd.DataFrame(data = {"match_id":b.index.get_level_values(0), "player":b.index.get_level_values(1), "runs_scored":b.values})

df["total_runs"] = df["total_runs"] - df["extra_runs"] + df["wide_runs"]
d1 = df.groupby(["match_id", "bowler"])["total_runs"].agg("sum")
df1= pd.DataFrame(data = {"match_id":d1.index.get_level_values(0), "player":d1.index.get_level_values(1), "runs_conceded":d1.values})

df = df[(df["dismissal_kind"] != "run out") & (df["dismissal_kind"] != "obstructing the field") & (df["dismissal_kind"] != "retired hurt")]
d2 = df.groupby(["match_id", "bowler"])["player_dismissed"].agg("count")
df2 = pd.DataFrame(data = {"match_id":d2.index.get_level_values(0), "player":d2.index.get_level_values(1), "wickets":d2.values})

df3 = pd.merge(df1, df2, on = ["match_id", "player"])
df5 = pd.merge(df4, df3, on = ["match_id", "player"])
df5
