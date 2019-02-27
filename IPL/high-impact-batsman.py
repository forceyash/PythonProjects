#high-impact-batsman
import pandas as pd

df = pd.read_csv("C:\\Users\\yash.a.mishra\\AppData\\Local\\Programs\\Python\\Python37\\Machine Learning\\Pandas\\ipl\\deliveries.csv")
df = df[df.is_super_over != 1]
d1 = df.groupby(["batsman"])["batsman_runs"].agg("sum") #Runs
d3 = df.groupby(["batsman"])["batsman"].agg("count") #Balls
df = df[(df.batsman == df.player_dismissed) | (df.player_dismissed == "")]
d2 = df.groupby(["batsman"])["player_dismissed"].agg("count") #no of times dismissed
df2 = pd.DataFrame(data = {"batsman": d1.index.values, "runs": d1.values})
df3 = pd.DataFrame(data = {"batsman": d2.index.values, "out": d2.values})
df4 = pd.DataFrame(data = {"batsman": d3.index.values, "balls": d3.values})
df2 = pd.merge(df2, df3, on = "batsman")
df2 = pd.merge(df2, df4, on = "batsman")
df2 = df2[df2.runs >= 1000] #minimum 1000 runs
df2["impact"] = (df2.runs/df2.out) + ((df2.runs/df2.balls)*100)
print(df2.nlargest(20, "impact"))
