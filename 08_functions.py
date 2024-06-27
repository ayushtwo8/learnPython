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


# lambda function: it is a small anonymous function.

x = lambda a : a + 10
print(x(5))


x = lambda a,b : a*b
print(x(5,6))


def myfunc(n):
    return lambda a:a*n
mydoubler = myfunc(2)
print(mydoubler(11))

# use lambda functions when an anonymous function is required
# for a short period of time.

