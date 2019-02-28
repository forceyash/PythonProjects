#batsman-boundary-percentage
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv("C:\\Users\\Yash\\AppData\\Local\\Programs\\Python\\Python36-32\\Machine Learning\\IPL\\deliveries.csv")
z = df.groupby("batsman")["batsman_runs"].apply(lambda x: x.value_counts()).unstack().reset_index().fillna(0)
z["Runs"] = z[1] + z[2]*2 + z[3]*3 + z[4]*4 + z[5]*5 + z[6]*6
z["Balls"] = z[[0,1,2,3,4,5,6]].sum(1)
z["bndry_pct"] = np.round((z[4]*4 + z[6]*6)/z["Runs"]*100, 2)
z["1s-2s_pct"] = np.round((z[1]+z[2]*2)/z["Runs"]*100, 2)
z["dots_pct"] = np.round(z[0]/z["Runs"]*100, 2)
z.fillna(0, inplace=True)
#z.sort_values(by = ["Runs", "dots_pct"], ascending = [False, False])
#z.nlargest(20, "Runs").nlargest(20, "dots_pct")
z.nlargest(20, "Runs").nlargest(20, "bndry_pct")

"""
-----------------------------------------
Analysis about top 20 run getters in IPL
-----------------------------------------

most runs in boundries: CH Gayle  - 76.25%
most runs in 1s and 2s: JH Kallis - 45.90%
most dot balls        : JH Kallis - 40.46%

"""
