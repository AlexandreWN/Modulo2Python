"""
import pandas as pd

titanic = pd.read_csv("./Docs/train.csv", sep=",")

filtro = (titanic["Pclass"] == 1) & (titanic["Survived"] == 1) | (titanic["Pclass"] == 3) & (titanic["Survived"] == 0)

print(titanic[filtro])

"""

import pandas as pd

titanic = pd.read_csv("./Docs/train.csv", sep=",")

filtro = ((titanic["Embarked"] == "S") & (titanic["Pclass"] == 2) & (titanic["Age"] == 29) & (titanic["Name"].str.contains("Anne")))

pessoa = titanic[filtro]

if(pessoa.iloc[0, :]["Survived"]==1):
    print("Ta viva")
else:
    print("Ta morta")
    