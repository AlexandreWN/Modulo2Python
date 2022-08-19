import numpy as np
from numpy.random import default_rng

rng = default_rng()
x = np.random.randint(0,10,49).reshape((7,7))

print("Matriz original")
print(x,"\n")

print("Matriz modificado com numeros maiores que 3 e menores que 8 substituidos por (a)")
x= np.where((x > 3) & (x < 8), 'a', x)
print(x)