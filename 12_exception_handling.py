# try block lets you test a block  of code for errors. 
# except block lets you handle the error. 
# else block lets you execute the code when there is no error.
# finally block lets you execute code, regardless of the result 
# of try and except blocks.

#example 1

try:
    print(x)
except NameError:
    print("Variable x is not defined")  
except:
    print("Something else went wrong")    
else:
    print("Nothing wrong")    


# example 2

try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")   
finally:
    print("The 'try except' is finished")


# example 3 - raise an exception

num = -1

if num<0:
    raise Exception("Sorry, no numbers below zero")

# example 4 - raise a TypeError

t = "Mohan"

if not type(t) is int:
    raise TypeError("Only integers are allowed")