import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

'''
df = pd.read_csv("C:\\Users\\yash.a.mishra\\AppData\\Local\\Programs\\Python\\Python37\\Machine Learning\\Pandas\\ipl\\deliveries.csv")
df_matches = pd.read_csv("C:\\Users\\yash.a.mishra\\AppData\\Local\\Programs\\Python\\Python37\\Machine Learning\\Pandas\\ipl\\matches.csv")
df = pd.merge(df, df_matches[["match_id", "season"]], on="match_id")
#player = input("Enter a player: ")
df = df[["match_id", "inning", "season", "batsman", "batsman_runs", "non_striker", "player_dismissed", "over", "ball"]]
df_whole = df
df = df[(df.player_dismissed.notnull()) | ((df.over == 20) & (df.ball == 6))]
df_player = pd.DataFrame(columns = ["match_id", "innings", "batsman", "position"])
g1 = df.groupby(["match_id", "inning", "batsman"])["batsman_runs"].agg("count")
d1 = pd.DataFrame(data = {"match_id": g1.index.get_level_values(0), "innings": g1.index.get_level_values(1), "batsman": g1.index.get_level_values(2)})
g2 = df.groupby(["match_id", "inning", "non_striker"])["batsman_runs"].agg("count")
d2 = pd.DataFrame(data = {"match_id": g2.index.get_level_values(0), "innings": g2.index.get_level_values(1), "batsman": g2.index.get_level_values(2)})
df_player = df_player.append(d1)
df_player = df_player.append(d2)
df_player = df_player.drop_duplicates()
df_player = df_player.sort_values(by = ["match_id", "innings"])

#print(np.where((df_player["batsman"] == "DA Warner") & (df_player["match_id"] == 1) & (df_player["innings"] == 1))[0][0])
len_df = len(df)
i = 0
pos = 1
while(i < len_df):
    match_id = df.iloc[i]["match_id"]
    innings = df.iloc[i]["inning"]
    batsman = df.iloc[i]["batsman"]
    non_striker = df.iloc[i]["non_striker"]
    x = np.where((df_player["batsman"] == batsman) & (df_player["match_id"] == match_id) & (df_player["innings"] == innings))[0][0]
    if (pd.isnull(df_player.iloc[x]["position"]) & (x != "")):
        df_player.iloc[x]["position"] = pos
        pos = pos + 1

    x = np.where((df_player["batsman"] == non_striker) & (df_player["match_id"] == match_id) & (df_player["innings"] == innings))[0][0]
    if (pd.isnull(df_player.iloc[x]["position"]) & (x != "")):
        df_player.iloc[x]["position"] = pos
        pos = pos + 1

    if(i < (len_df - 1)):
        if((df.iloc[i+1]["inning"] != innings) | (pos > 11) | (df.iloc[i+1]["match_id"] != match_id)):
            pos = 1

    i = i + 1


df_player["match_id"] = df_player["match_id"].apply(int)
df_whole = pd.merge(df_whole, df_player, on = (["match_id", "batsman"]))
df_whole = df_whole[df_whole.batsman == "DA Warner"]
df_whole["position"] = df_whole["position"].replace(2, 1)
print(df_whole.groupby(["position", "batsman"])["batsman_runs"].agg("sum"))
'''
#temp = df_whole.groupby(["position", "batsman"])["batsman_runs"].agg("sum")
#print(temp.groupby(level=0).nlargest(5).reset_index(level=0, drop=True))
#********************************************************************************************************************
deliveries = pd.read_csv("C:\\Users\\yash.a.mishra\\AppData\\Local\\Programs\\Python\\Python37\\Machine Learning\\Pandas\\ipl\\deliveries.csv")
#print(deliveries.groupby(['match_id', 'inning']).batsman.apply(lambda x: dict(x[~x.duplicated()])))
mapper = deliveries.groupby(['match_id', 'inning']).batsman.apply(lambda x: dict(zip(x[~x.duplicated()], np.arange(1, len(x[~x.duplicated()])+1)))).reset_index(name = 'batting_position').rename(columns = {'level_2':'batsman'})
#print(mapper)
deliveries_position = deliveries.merge(mapper, on = ['match_id', 'inning', 'batsman'], how = 'outer')
deliveries_position["batting_position"] = deliveries_position["batting_position"].replace(2, 1)
temp = deliveries_position.groupby(["batting_position", "batsman"])["batsman_runs"].agg("sum")
print(temp.groupby(level=0).nlargest(5).reset_index(level=0, drop=True))
