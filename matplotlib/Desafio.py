import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./Docs/respiradores.csv')

regiaoNorte=df.loc[:,["AMAZONAS", "AMAPA", "RORAIMA", "ACRE", "PARA", "RONDONIA", "TOCANTINS"]]
regiaoNordeste=df.loc[:,["MARANHÃO","PIAUI","RIO GRANDE DO NORTE","CEARA","PARAIBA","BAHIA","PERNAMBUCO","ALAGOAS","SERGIPE"]]
regiaoCentroOeste=df.loc[:,["GOIAS","MATO GROSSO ","MATO GROSSO DO SUL","DISTRITO FEDERAL"]]
regiaoSudeste=df.loc[:,["MINAS GERAIS","ESPIRITO SANTO ","RIO DE JANEIRO","SÃO PAULO"]]
regiaoSul=df.loc[:,["PARANA", "RIO GRANDE DO SUL ", "SANTA CATARINA"]]


#Soma total das regiões
totalNorte = regiaoNorte.sum().sum()
totalNordeste = regiaoNordeste.sum().sum()
totalCentroOeste = regiaoCentroOeste.sum().sum()
totalSudeste = regiaoSudeste.sum().sum()
totalSul = regiaoSul.sum().sum()

x=["Norte", "Nordeste", "Centro Oeste", "Sudeste", "Sul"]
y=[totalNorte,totalNordeste,totalCentroOeste,totalSudeste,totalSul]
plt.bar(x,y)
plt.title("COMPRA DE RESPIRADORES TOTAL POR REGIÃO")
plt.xticks(rotation = '90')
plt.yticks(rotation = '45')
plt.show()



#soma total estado por mes
totalNorte = regiaoNorte.sum(axis = 1)
totalNordeste = regiaoNordeste.sum(axis = 1)
totalCentroOeste = regiaoCentroOeste.sum(axis = 1)
totalSudeste = regiaoSudeste.sum(axis = 1)
totalSul = regiaoSul.sum(axis = 1)

x=df.MES
plt.plot(x,totalNorte)
plt.plot(x,totalNordeste)
plt.plot(x,totalCentroOeste)
plt.plot(x,totalSudeste)
plt.plot(x,totalSul)
plt.title("COMPRA DE RESPIRADORES POR MÊS POR ESTADO")
plt.xticks(rotation = '90')
plt.yticks(rotation = '45')
plt.legend(["Norte", "Nordeste", "Centro Oeste", "Sudeste", "Sul"]) 
plt.show()


