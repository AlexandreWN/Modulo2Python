import pandas as pd

titanic = pd.read_csv("./Docs/train.csv", sep=",")

#print(titanic.Survived[titanic["Survived"] == 0].count())
#print(titanic.Survived[titanic["Survived"] == 1].count())

def calculate_percentage(val, total):
    percent = float(val / total)
    beautiful_percent = ("%.2f" % (percent * 100) + "%")
    return beautiful_percent

total = titanic.Survived.count()


'''Taxa de sobrevivencia por classe'''

#Sobrevivel Primeira Classe
sobreviveuPrimeira = titanic[(titanic["Pclass"] == 2) & (titanic["Survived"] == 1)]['Survived'].count()
#Sobrevivel Segunda Classe
sobreviveuSegunda = titanic[(titanic["Pclass"] == 2) & (titanic["Survived"] == 1)]['Survived'].count()
#Sobrevivel Terceira Classe
sobreviveuTerceira = titanic[(titanic["Pclass"] == 3) & (titanic["Survived"] == 1)]['Survived'].count()

#Total Primeira Classe Embarcados
totalPrimeira = titanic[(titanic["Pclass"] == 1)]['Pclass'].count()
#Total Segunda Classe Embarcados
totalSegunda = titanic[(titanic["Pclass"] == 2)]['Pclass'].count()
#Total Terceira Classe Embarcados
totalTerceira = titanic[(titanic["Pclass"] == 3)]['Pclass'].count()
'''
print("Sobrvivel da primeira classe", calculate_percentage(sobreviveuPrimeira, totalPrimeira))
print("Sobrvivel da segunda classe", calculate_percentage(sobreviveuSegunda, totalSegunda))
print("Sobrvivel da terceira classe", calculate_percentage(sobreviveuTerceira, totalTerceira))
'''

'''Taxa de sobrevivencia por idade'''

def faixa_etaria(linhas):
    idade = linhas["Age"]
    if idade < 12:
        return "criança"
    elif idade >=12 and idade < 18:
        return "adolescente"
    elif idade >=18 and idade < 65:
        return "adulto"
    elif idade >= 65:
        return "idoso"
    else:
        return "nada"
        
titanic["faixa_etaria"] = titanic.apply(faixa_etaria, axis=1)

c = titanic["faixa_etaria"] == "criança"

mortos = titanic[titanic["Survived"] == 0]
vivos = titanic[titanic["Survived"] == 1]

filtro_mulher = titanic.Sex == 'female'
filtro_crianca = titanic.faixa_etaria == 'criança'

print("Morreram ",mortos.Survived[filtro_mulher | filtro_crianca].count()," mulheres/ crianças")
print("Sobreviveram ",vivos.Survived[filtro_mulher | filtro_crianca].count()," mulheres/ crianças")