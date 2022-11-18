import pandas as pd
df = pd.read_csv("elpris.csv")
#print(df)

cur = 0

df_new = df.loc[df.index[cur], 'Pris']

print(df_new)