#most runs while chasing

import pandas as pd

df = pd.read_csv("C:\\Users\\yash.a.mishra\\AppData\\Local\\Programs\\Python\\Python37\\Machine Learning\\Pandas\\ipl\\deliveries.csv")
df = df[df.is_super_over != 1]
df = df[df.inning == 2]
print(df.groupby(["batsman"])["batsman_runs"].agg("sum").nlargest(20))
