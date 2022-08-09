import numpy as np

x = np.array([[1,2,3],[4,5,6]])

print("Array padrão")
print(x)
print("\n")

print("Reshape")
x = x.reshape(3,2)
print(x)
print("\n")

print("Soma prmeira linha por 5")
x[0] = x[0] + 5
print(x)
print("\n")

print("multiplique a segunda linha por 3")
x[1] = x[1] * 3
print(x)
print("\n")

print("divida a segunda coluna por 2")
x[:2,1] = x[:2,1] / 2
print(x)
print("\n")