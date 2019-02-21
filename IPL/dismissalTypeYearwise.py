import pandas as pd
import numpy as np
df_deliv = pd.read_csv("deliveries.csv")
df_match = pd.read_csv("matches.csv")
df_deliv = df_deliv[["match_id", "dismissal_kind"]]
df_deliv.dropna(axis = 0, inplace = True)
df_group = pd.DataFrame(index = df_match["season"].unique(),columns = df_deliv["dismissal_kind"].unique())
df_group.fillna(0, axis = 0, inplace = True)

Len_of_df_deliv = len(df_deliv)
i = 0

while(i < Len_of_df_deliv):
    mode = df_deliv.iloc[i]["dismissal_kind"]
    mct_id = df_deliv.iloc[i]["match_id"]
    season = df_match.iloc[mct_id-1]["season"]
    p = df_group.iloc[df_group.index.get_loc(season), df_group.columns.get_loc(mode)] + np.int64(1)
    df_group.iat[df_group.index.get_loc(season), df_group.columns.get_loc(mode)] = p
    i=i+1

print(df_group)
