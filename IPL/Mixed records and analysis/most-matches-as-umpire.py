#Most experienced umpires
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv("C:\\Users\\yash.a.mishra\\AppData\\Local\\Programs\\Python\\Python37\\Machine Learning\\Pandas\\ipl\\matches.csv")
umps = np.concatenate((df["umpire1"].values, df["umpire2"].values), axis = 0)
#print(umps)
print(pd.Series(umps).value_counts().reset_index().rename(columns = {"index": "Umpire", 0: "Matches"}))

"""
Output(top 10)

                   Umpire  Matches
0         HDPK Dharmasena       87
1                  S Ravi       85
2            AK Chaudhary       58
3           C Shamshuddin       56
4              SJA Taufel       55
5               M Erasmus       54
6               Asad Rauf       51
7             BR Doctrove       42
8             RE Koertzen       41
9               CK Nandan       41
10            VA Kulkarni       39

"""
