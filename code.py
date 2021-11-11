import pandas as pd 

df = pd.read_csv("total_stars.csv")
print(df.columns)
print(df.shape)
del df ["Luminosity"]
del df ["Star_name"]
del df ["Distance"]
del df ["Mass"]
del df ["Radius"]
del df ["Unnamed: 0"]
del df ["Unnamed: 6"]

print(df.columns)
df.to_csv("Final.csv")
