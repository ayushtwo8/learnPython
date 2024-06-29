# JSON is a syntax for storing and exchanging data.
# JSON is a text, written with Javascript object notation. 

import json

# some json
x = '{"name":"John", "age":25, "city":"New York"}'

# parse x: convert from json to python
y = json.loads(x)

# the result is a python dictionary
print(x)
print(y)
print(y["age"])

# convert from python to JSON
a = {
    "name":"Agastya",
    "age":"30",
    "city":"New York"
}

# b = json.dumps(a) 
b = json.dumps(a,indent=4, separators=(", ","= ")) #with some more attributes
# the result is a JSON string
print(b)
print(type(b))

# when you convert from python to json, python objects are converted into the
# JSON equivalent:

"""

Python       JSON
    
dict	     Object
list	     Array
tuple	     Array
str	         String
int	         Number
float	     Number
True	     true
False	     false
None	     null

"""

# Python RegEx: Regular expression is a sequence of character that forms a search pattern. 


import re #regex module
txt = "The girl on the train"
p = re.search("^The.*train$",txt)  # search the string to see if it starts with "The" and ends with "train"

print(p)

""" 

RegEx functions

Functions    Description

findall	     Returns a list containing all matches
search	     Returns a Match object if there is a match anywhere in the string
split	     Returns a list where the string has been split at each match
sub	         Replaces one or many matches with a string

"""
# Read more about regex at https://www.w3schools.com/python/python_regex.asp