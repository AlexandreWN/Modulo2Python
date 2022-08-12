import matplotlib.pyplot as plt 
import numpy as np 
import math 
X = np.arange(0, math.pi*2, 0.05) 
Y1 = np.sin(X) 
Y2 = np.cos(X) 


plt.figure(figsize = ((12, 6)))

plt.subplot(1, 2, 1) 
plt.plot(X, Y1) 

plt.subplot(1, 2, 2) 
plt.plot(X, Y2) 
plt.show() 