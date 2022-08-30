import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn import preprocessing
import numpy as np

dados = {'Tempo':["Ensolarado","Ensolarado","Nublado","Chuvoso","Chuvoso","Chuvoso","Nublado","Ensolarado","Ensolarado","Chuvoso"],
    'Umidade':["Alta","Alta","Alta","Alta","Normal","Normal","Normal","Alta","Normal","Normal"],
    'Vento':["Fraco","Forte","Fraco","Fraco","Fraco","Forte","Forte","Fraco","Fraco","Fraco"],
    'Treinou':["Não","Não","Sim","Sim","Sim","Não","Sim","Não","Sim","Sim"]}

dados = pd.DataFrame(data=dados)

#criando o labelEncoder
tempo = preprocessing.LabelEncoder()
umidade = preprocessing.LabelEncoder()
vento = preprocessing.LabelEncoder()
treinou = preprocessing.LabelEncoder()

#atribuindo numeros as variaveis qualitativas
tempo.fit(dados['Tempo'].unique())
umidade.fit(dados['Umidade'].unique())
vento.fit(dados['Vento'].unique())
treinou.fit(dados['Treinou'].unique())

#transformando o data set de variaveis qualitativas para quantitativas
dados['Tempo'] = tempo.transform(dados['Tempo'])
dados['Umidade'] = umidade.transform(dados['Umidade'])
dados['Vento'] = vento.transform(dados['Vento'])
dados['Treinou'] = treinou.transform(dados['Treinou'])

#separando data set nos atributos previsores e na classe objetivo
previsor = dados[['Tempo', 'Umidade', 'Vento']]
classe = dados['Treinou']

#Criando classificação NaiveBayes
gnb = GaussianNB()
gnb.fit(previsor, classe)

#verificando precisão
print("precisão =", gnb.score(previsor, classe)*100,"%")

#inserindo os dados para serem previstos
previsao = {'Tempo':['Ensolarado', 'Nublado', 'Nublado', 'Chuvoso'], 'Umidade':['Normal', 'Alta', 'Normal', 'Alta'], 'Vento':['Forte', 'Forte', 'Fraco', 'Forte']}
previsao = pd.DataFrame(data=previsao)

previsao['Tempo'] = tempo.transform(previsao['Tempo'])
previsao['Umidade'] = umidade.transform(previsao['Umidade'])
previsao['Vento'] = vento.transform(previsao['Vento'])

#verificando resultado
print(gnb.predict(previsao))
print(treinou.inverse_transform(gnb.predict(previsao)))

#verificando probabilidades
result = gnb.predict_proba(previsao)
print(np.array([i * 100 for i in result]))