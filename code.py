import pandas as pd 

df = pd.read_csv("total_stars.csv")
print(df.columns)
print(df.shape)
del df ["Luminosity"]

print(df.columns)
df.to_csv("Final.csv")