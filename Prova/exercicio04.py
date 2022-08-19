import matplotlib.pyplot as plt 
import numpy as np 

x = np.linspace(-20,20,400)
y = x**2
fig = plt.figure(figsize = ((12, 6)))
ax = fig.add_subplot(1, 1, 1)

plt.subplot(1,2,1)
plt.grid(linestyle='solid')
plt.plot(x,y, 'r')


Y = x**3

plt.subplot(1, 2, 2) 
plt.grid(linestyle='solid')
plt.plot(x, Y, 'r') 
plt.show() 