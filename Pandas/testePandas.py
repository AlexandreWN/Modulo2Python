import pandas as pd

train = pd.read_csv("./Docs/train.csv", sep=",")

#Primeiros 5
print(train.head())

print("\n")

#ultimos 5
print(train.tail())