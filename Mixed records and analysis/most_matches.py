import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

deliveries = pd.read_csv("C:\\Users\\yash.a.mishra\\AppData\\Local\\Programs\\Python\\Python37\\Machine Learning\\Pandas\\ipl\\deliveries.csv")
#mapper = deliveries.groupby(['match_id', 'inning']).batsman.apply(lambda x: dict(zip(x[~x.duplicated()], np.arange(1, len(x[~x.duplicated()])+1)))).reset_index(name = 'batting_position').rename(columns = {'level_2':'batsman'})

players = pd.DataFrame(columns=("match_id", "player"))
i=0
def func1(x):
    batters = x.batsman.unique()
    bowlers = x.bowler.unique()
    fielder = x.fielder.unique()
    All = np.concatenate((batters, bowlers, fielder))
    All = pd.Series(np.array(All).tolist()).drop_duplicates()
    return pd.DataFrame(data = {"players": All})

mapper = deliveries.groupby('match_id')["batsman", "bowler", "fielder"].apply(lambda x: func1(x)).reset_index().drop("level_1", axis = 1).dropna()
print(mapper.groupby('players').match_id.count().nlargest(30))
