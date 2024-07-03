# Generate a 1D array containing 5 random integers from 0 to 100.
from numpy import random
x = random.randint(100, size=(5))
print(x)


# rand() method returns a random float number between 0 and 1.
num = random.rand()
print(num)


# Generate a 2D array with 3 rows and each row containing 5 random
# integers from 0 to 100:

a = random.randint(100,size=(3,5))
print(a)


# Return one of the values in an array:

b = random.choice([3,4,7,9])
print(b)