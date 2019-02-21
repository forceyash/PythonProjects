import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

deliveries = pd.read_csv("C:\\Users\\Yash\\AppData\\Local\\Programs\\Python\\Python36-32\\Machine Learning\\IPL\\deliveries.csv")
df_matches = pd.read_csv("C:\\Users\\Yash\\AppData\\Local\\Programs\\Python\\Python36-32\\Machine Learning\\IPL\\matches.csv")
mapper = deliveries.groupby(['match_id', 'inning']).batsman.apply(lambda x: dict(zip(x[~x.duplicated()], np.arange(1, len(x[~x.duplicated()])+1)))).reset_index(name = 'batting_position').rename(columns = {'level_2':'batsman'})

deliveries_position = deliveries.merge(mapper, on = ['match_id', 'inning', 'batsman'], how = 'outer')
print(deliveries_position)
