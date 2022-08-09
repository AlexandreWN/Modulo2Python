import numpy as np

x = np.array([[1,2,3],[4,5,6],[7,8,9]])

print("Matriz original")
print(x,"\n")

print("Matriz com os impares substituidos por 0")
x[x % 2 != 0] = 0
print(x)

