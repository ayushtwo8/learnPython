# Randomly shuffle elements of following array:
from numpy import random
import numpy as np

arr = np.array([1,2,3,4,5])

random.shuffle(arr) #changes original array

print(arr)


# Generating permutations of arrays

print(random.permutation(arr)) #doesn't changes original array

print(arr)