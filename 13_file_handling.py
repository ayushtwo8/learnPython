"""
The key function for working with files in python is the open() function.

There are four methods of opening a file:
r - read
a - append
w - write (will overwrite any existing content)
x - create

t - text mode
b - binary mode

"""

# to create and write something on it

f = open("myfile.txt", "w")
f.write("Hello! Welcome to demofile.\nThis file is for testing purpose only.")
f.close()

# to read file 

f = open("myfile.txt","r")
print(f.read())
f.close()

# to delete file

import os
os.remove("myfile.txt")
