# Draw a line in a diagram from position (0,0) to position (6,250). 

import matplotlib.pyplot as plt 
import numpy as np 

xpoints = np.array([0,6])
ypoints = np.array([0,250])

plt.plot(xpoints, ypoints, marker = "+")
plt.show()


# Draw a line in a diagram from position (1,3) to (2,8) then to (6,1) 
# and finally to position (8,10). 

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1,2,6,8])
ypoints = np.array([3,8,1,10])

plt.plot(xpoints, ypoints, marker = "o", linestyle = 'dotted')
plt.show()


# Add labels to the x and y axis. 

import numpy as np 
import matplotlib.pyplot as plt

x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])

plt.plot(x,y)

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.grid()

plt.show()


# display multiple plots

import matplotlib.pyplot as plt
import numpy as np 

#plot 1:
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])

plt.subplot(1,2,1)
plt.plot(x,y)
plt.title("SALES")

#plot 2:
x = np.array([0,1,2,3])
y = ([10,20,30,40])

plt.subplot(1,2,2)
plt.plot(x,y)
plt.title("INCOME")


plt.suptitle("MY SHOP")
plt.show()