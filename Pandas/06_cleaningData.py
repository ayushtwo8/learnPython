import pandas as pd

df = pd.read_csv('Player.csv')
new_df = df.dropna()
print(new_df.to_string())
df.dropna(inplace=True) # If you want to change the original dataframe, use the inplace=True
print(df.to_string())

# Replace empty values

df.fillna(130, inplace=True)
print(df)



