import pandas as pd

myDataset = {
    'car' : ["BMW","Volvo","Ford"],
    'passings' : [3,7,2]
}

myVar = pd.DataFrame(myDataset)

print(myVar)

# checking pandas version

print(pd.__version__)