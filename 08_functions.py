# Function: a block of code which only runs when it is called.abs

def greet(name):
    print(f"Hello, {name}!!")

greet("Khushi")    

# Arbitrary arguments: *args 

def func(*kids):
    print(f"The youngest kid is {kids[2]}")

func("emi","rohan","john","doe")

# Arbitrary keyword arguments: **kwargs

def oneFunct(**kid):
    print(f"His last name is {kid["lname"]}")

oneFunct(fname = "John", lname = "Doe")    