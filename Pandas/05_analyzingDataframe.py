# head() method returns the headers and a specified numbers of rows, starting from the top.

import pandas as pd
df = pd.read_csv('Player.csv')
print(df.head(10))
print(df.tail())
print(df.info())
