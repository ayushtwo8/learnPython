print("Hello, Python!!")

# This is a single line comment in python.

#----------Variables----------#

x = 5
y = "john"

a = str(3)
b = int(3)
c = float(3)


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
value7 = range(6)
value8 = {"name":"rohan","age":25}
value9 = {"carrot","cabbage","brinjal"}
value10 = frozenset({"apple","banana","cherry"})
value11 = True
value12 = b"Hello"
value13 = bytearray(5)
value14 = memoryview(bytes(5))
value15 = None

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


# Random Number - random module is used to generate a random number in python

import random
print(random.randrange(1,10))

# Strings - Strings in python are arrays of bytes representing unicode characters

str1 = "Hello, Ayush"
print(str1[1])

for i in "banana":
    print(i)

print(len(str1))  # to find the length of a string
print("hello" in str1) #checking string

# Slicing string

str2 = " This is a sample string."
print(str2[2:20])
print(str2[:20]) #slice from the start
print(str2[10:]) #slice from the end
print(str2[-15:-5]) #Negative indexing
print(str2.upper()) #Upper case 
print(str2.lower()) #Lower case
print(str2.strip()) #remove whitespace
print(str2.replace("sample","premium")) #replace
print(str2.split(" ")) #split string on the basis of space

# String concatenation
str3 = "Radhe"
str4 = "Shyam"
str5 = str3 + str4
str6 = str3 +" "+ str4
print(str6)

#String format
age = 45
# txt = "Rahul's age is " + age #we can't combine number and string like this
txt1 = f"Rahul's age is {age}" #F-Strings in pythn
print(txt1)