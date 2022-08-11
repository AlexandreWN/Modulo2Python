import pandas as pd

train = pd.read_csv("./Docs/train.csv", sep=",")

#Primeiros 5
#print(train.head())

print("\n")
#ultimos 5
print(train.tail())
print("\n")
#traz a coluna
print(train["Name"].head())
colunas_selecionadas = ["PassengerId","SibSp","Parch"]
print(train[colunas_selecionadas].head())
print(train[["Age","Pclass"]].describe())

print(train.loc[:13,["Age"]])

print(train["Embarked"].unique()) #Podemos verificar todos os valores unicos

print(train["Age"].value_counts()) #Contagem de quantas vezes eles aparecem, normalize