import matplotlib.pyplot as plt
import numpy as np
import math

# 100 linearly spaced numbers
x = np.linspace(-20,20,400)

# the function, which is y = x^2 here
y = x**2

# setting the axes at the centre
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# plot the function
plt.plot(x,y, 'r')

# show the plot
plt.show()

