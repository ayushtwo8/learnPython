# Generate a random normals distribution of size 2X3:

from numpy import random
x = random.normal(size=(2,3))
print(x)


# Generate a random normal distribution of size 2x3 with mean at 1 and standard deviation of 2:

y = random.normal(loc=1, scale=2, size=(2,3))
print(y)


# Visualization of normal distribution

import matplotlib.pyplot as plt
import seaborn as sns  

sns.distplot(random.normal(size=1000), hist=False)
plt.show()



# WILL BE CONTINUED LATER...