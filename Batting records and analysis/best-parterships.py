import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

deliveries = pd.read_csv("C:\\Users\\Yash\\AppData\\Local\\Programs\\Python\\Python36-32\\Machine Learning\\IPL\\deliveries.csv")
df_matches = pd.read_csv("C:\\Users\\Yash\\AppData\\Local\\Programs\\Python\\Python36-32\\Machine Learning\\IPL\\matches.csv")
deliveries[["batsman", "non_striker"]] = np.sort(deliveries[["batsman", "non_striker"]], 1)

mapper = deliveries.groupby(["batsman", "non_striker"]).batsman_runs.agg("sum")
mapper.nlargest(20)
