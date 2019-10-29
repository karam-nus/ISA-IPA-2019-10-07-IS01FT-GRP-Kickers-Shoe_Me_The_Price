import pandas as pd


df = pd.DataFrame(columns=['Name','age'])
d ={"Name": "Kartik", "age":10}

df =df.append(d, ignore_index=True)
df =df.append(d, ignore_index=True)
df =df.append(d, ignore_index=True)

print(df.iloc[0])

a = df.iloc[0]

print(a['Name'])