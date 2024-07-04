# Create a dataframe from two sets:
import pandas as pd
data = {
    "calories" : [420,380,390],
    "duration" : [40,40,45]
}
Var = pd.DataFrame(data)

print(Var)

print(Var.loc[0])
print(Var.loc[[0,1]])