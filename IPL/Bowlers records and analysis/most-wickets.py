import pandas as pd
df = pd.read_csv("C:\\Users\\Yash\\AppData\\Local\\Programs\\Python\\Python36-32\\Machine Learning\\IPL\\deliveries.csv")
df = df[(df["is_super_over"] != 1)]
df = df[df.player_dismissed.notnull()]
df = df[(df["dismissal_kind"] != "run out") & (df["dismissal_kind"] != "obstructing the field") & (df["dismissal_kind"] != "retired hurt")]
df["bowler"].value_counts()
