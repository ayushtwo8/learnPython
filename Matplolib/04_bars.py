# Draw 4 bars:

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A","B","C","D"])
y = np.array([3,8,1,10])

plt.bar(x,y, color = "green")
plt.show()

# Histogram

import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170,10,250)

plt.hist(x)

plt.show()


# Pie charts

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35,25,25,15])
mylabels = ["Apples","Bananas","Cherries","Dates"]
myexplode = [0.1,0,0,0]

plt.pie(y, labels = mylabels, explode = myexplode)
plt.legend("Four fruits: ")
plt.show()