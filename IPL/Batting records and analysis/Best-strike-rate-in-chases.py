#Best-strike-rate-in-chases
import pandas as pd

df = pd.read_csv("C:\\Users\\yash.a.mishra\\AppData\\Local\\Programs\\Python\\Python37\\Machine Learning\\Pandas\\ipl\\deliveries.csv")
df = df[df.is_super_over != 1]
df = df[df.inning != 1]
d1 = df.groupby(["batsman"])["batsman_runs"].agg("sum")
d2 = df.groupby(["batsman"])["batsman"].agg("count")
df3 = pd.DataFrame(data = {"batsman": d2.index.values, "balls": d2.values})
df2 = pd.DataFrame(data = {"batsman": d1.index.values, "runs": d1.values})
df2 = pd.merge(df2, df3, on = "batsman")
df2 = df2[df2.balls >= 1000]
df2["strike_rate"] = (df2.runs/df2.balls)*100
print(df2.nlargest(20, "strike_rate"))
