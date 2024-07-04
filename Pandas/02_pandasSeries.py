# create a simple pandas series from a list

import pandas as pd
a = [1,7,2]

myVar = pd.Series(a)
print(myVar)

# or 

myVar = pd.Series(a,index = ["x","y","z"])
print(myVar)


