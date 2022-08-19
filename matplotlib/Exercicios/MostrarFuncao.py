import matplotlib.pyplot as plt
import numpy as np
import math

x = np.linspace(-20,20,400)

y = x**2

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

plt.plot(x,y, 'r')

plt.show()

