# NumPy is a python library.
# NumPy is used for working with arrays.
# NumPy is short for "Numerical Python". 


# Create a numpy array.

import numpy as np 
print(np.__version__)
arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))


# Use a tuple to create a numpy array

import numpy as np
arr = np.array((1,2,3,4,5))
print(arr)


# 0D, 1D, 2D array

arr0 = np.array(45) # 0D array
arr1 = np.array([1,2,4,5,6])  # 1D array
arr2 = np.array([[1,2,3,4],[5,5,2,6]])  # 2D array

print(arr0)
print(arr1)
print(arr2)

# printing dimensions
print(arr0.ndim)
print(arr1.ndim)
print(arr2.ndim)



# Slicing array

import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])
print(arr[1:5])
print(arr[-4:-1])
print(arr[1:7:2]) # [start : end : step]
print(arr[::3]) # return every other element from the entire array


# get the datatype of an array object

print(arr.dtype)


# Creating array with a defined datatype

strArr = np.array([1,2,3,4], dtype='S')
print(strArr)
print(arr.dtype)