import pandas as pd

df = pd.read_csv('countries.csv')
for i=0:i < df.size:i++:
    result = df.iloc[i]

print(result)