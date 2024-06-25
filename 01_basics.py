print("Hello, Python!!")

# This is a single line comment in python.

#----------Variables----------#

x = 5
y = "john"

a = str(3)
b = int(3)
c = float(3)

print(type(x))
print(type(y))
print(type(a))
print(type(b))
print(type(c))

# Unpack a list
fruits = ["apple","banana","orange"]
p,q,r = fruits
print(p)
print(q)
print(r)

#Global variables without using global keyword

var = "awesome"

def myfunc():
    print("Python is "+var)

myfunc()    

#Global variables using global keyword
def fun():
    global var1
    var1 = "fantastic"

fun()

print("Python is "+var1)