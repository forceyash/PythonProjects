import matplotlib.pyplot as plt
import numpy as np

deliveries = pd.read_csv("C:\\Users\\Yash\\AppData\\Local\\Programs\\Python\\Python36-32\\Machine Learning\\IPL\\deliveries.csv")
df_matches = pd.read_csv("C:\\Users\\Yash\\AppData\\Local\\Programs\\Python\\Python36-32\\Machine Learning\\IPL\\matches.csv")
mapper = deliveries.groupby(['match_id', 'inning']).batsman.apply(lambda x: dict(zip(x[~x.duplicated()], np.arange(1, len(x[~x.duplicated()])+1)))).reset_index(name = 'batting_position').rename(columns = {'level_2':'batsman'})

deliveries_position = deliveries.merge(mapper, on = ['match_id', 'inning', 'batsman'], how = 'outer')
deliveries_position = deliveries_position[(deliveries_position.batting_position == 8) |(deliveries_position.batting_position == 9)
                                         |(deliveries_position.batting_position == 10) | (deliveries_position.batting_position == 11)]
asBatsman = deliveries_position.groupby(["batsman", "batting_position"]).batsman_runs.agg({"Runs" : "sum"})#.nlargest(10, "Runs")
print(type(asBatsman))
temp = deliveries_position.drop_duplicates(subset = ["batsman","match_id"])
MatchesAtEachPosition = temp.groupby(["batsman","batting_position"]).match_id.agg({"matches": "count"})
print(type(MatchesAtEachPosition))
tmp = asBatsman.merge( MatchesAtEachPosition, how="outer", left_index = True, right_index = True)
tmp.nlargest(10, "Runs")                                                                               
print(deliveries_position)
