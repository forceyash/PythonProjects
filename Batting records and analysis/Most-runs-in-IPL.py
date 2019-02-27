import pandas as pd

df = pd.read_csv("deliveries.csv")
print(df.groupby("batsman")["batsman_runs"].agg("sum").nlargest(10))
