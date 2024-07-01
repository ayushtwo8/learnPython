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


# Create an array with datatype 4 bytes integer
intArr = np.array([1,2,3,4], dtype='i2')
print(intArr)
print(intArr.dtype)
print(len(intArr))


# Create datatype from float to integer by using 'i' as parameter value. 
intArray = np.array([1.1,2.1,3.1])
newarr = intArray.astype('i')

print(newarr)
print(newarr.dtype)



# Make a copy, change the original array, and display both arrays:

cArr = np.array([1,2,3,4,5,6])
x = cArr.copy()
cArr[0] = 45

print(cArr)
print(x) # the copy should not be affected by the changes 
# made to the original array.


# Make a view, change the original array, and display both arrays
vArr = np.array([1,2,3,4,5,6])
v = vArr.view()
vArr[0] = 45

print(vArr)
print(v) # the view should be affected by the changes made to 
# the original array


# Check if array owns its data
# Every numpy array has the attribute 'base' that returns 'None'
# if the array owns the data. 


# print the value of the base attribute to check if an array owns
# it's data or not. 

bArr = np.array([1,2,3,4,5])

a = bArr.copy()
b = bArr.view()

print(a.base)
print(b.base)

# get the shape of an array using shape attribute
sArr = np.array([[1,2,3,4],[5,7,4,6]])
print(sArr.shape)



# reshaping arrays from 1D to 2D
rArr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newArr = rArr.reshape(4,3)
print(newArr)

print(newArr.base)


# you are allowed to have one 'unknown dimension
# Convert 1D array with 8 elements to 3D array with 2x2 elements:

ukArr = np.array([1,2,3,4,5,6,7,8])
nukArr = ukArr.reshape(2,2,-1)
print(nukArr)



# flattening arrays: converting multidimensional arrays into 1D array 

fArr = np.array([[1,2,3],[4,5,6]])
newfArr = arr.reshape(-1)

print(newfArr)


# Iterating arrays using nditer()

# Iterating through the following 3D array:
iArr = np.array([[[1,2],[3,4],[5,6],[7,8]]])
for x in np.nditer(iArr):
    print(x)


# Iterating array with different datatypes:

# Iterate through the array as a string. 
nums = np.array([1,2,3])
for x in np.nditer(nums, flags=['buffered'],op_dtypes=['S']):
    print(x)


# Enumerated iteration using ndenumerate()

eArr = np.array([1,2,4])
for index, x in np.ndenumerate(eArr):
    print(index, x)



# Joining NumPy arrays 

# join two 1D arrays:

arrA = np.array([1,2,3])
arrB = np.array([4,5,6])
arrC = np.concatenate((arrA,arrB))
print(arrC)


# join two 2D arrays along rows(Axis = 1):

arrayA = np.array([[1,2],[3,4]])
arrayB = np.array([[5,6],[7,8]])
arrayC = np.concatenate((arrayA,arrayB), axis=1)
print(arrayC)