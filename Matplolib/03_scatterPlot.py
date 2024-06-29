# A simple scatter plot

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x,y)
plt.show()

# The observation in the example above is the result of 13 cars passing by.
# The X-axis shows how old the car is.
# The Y-axis shows the speed of the car when it passes.
# Are there any relationships between the observations?
# It seems that the newer the car, the faster it drives, but that could be a 
# coincidence, after all we only registered 13 cars.

import matplotlib.pyplot as plt
import numpy as np

# day 1, the age and the speed of 13 cars:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x,y, color = 'hotpink')

# day 2, the age and the speed of 15 cars:
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x,y, color = 'green')

plt.show()