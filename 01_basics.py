print("Hello, Python!!")

# This is a single line comment in python.

#----------Variables----------#

x = 5
y = "john"

a = str(3)
b = int(3)
c = float(3)


# Unpack a list
fruits = ["apple","banana","orange","mango"]
p,q,*r = fruits # *r is list contains all the left items
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

#----------DataTypes----------#

"""
Built-in datatypes:

Text type: str
Numeric types: int, float, complex
Sequence types: list, tuple, range
Mapping types: dict
Set types: set, frozenset
Boolean type: bool
Binary types: bytes, bytearray, memoryview
None type: noneType
"""

value1 = "Hello" 
value2 = 20
value3 = 30.5
value4 = 1j
value5 = ["apple","banana","mango"]
value6 = ("ram","sita","hanuman")
value7 = range(0,6)
value8 = {"name":"rohan","age":25}
value9 = {"carrot","cabbage","brinjal"}
value10 = frozenset({"apple","banana","cherry"})
value11 = True
value12 = b"Hello"
value13 = bytearray(5)
value14 = memoryview(bytes(5))
value15 = None
value16 = list(range(6))


print(type(value1))
print(type(value2))
print(type(value3))
print(type(value4))
print(type(value5))
print(type(value6))
print(type(value7))
print(type(value8))
print(type(value9))
print(type(value10))
print(type(value11))
print(type(value12))
print(type(value13))
print(type(value14))
print(type(value15))
print(value16)

# Random Number - random module is used to generate a random number in python

import random
print(random.randrange(1,10))

#isinstance(): Return whether an object is an instance of a class or of a subclass thereof.

num = 100
print(isinstance(num,int))

# Operators
num1 = 5
num2 = 2

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 % num2)
print(num1 ** num2)
print(num1 // num2)

print(num1 < 10 and num2 > 100)