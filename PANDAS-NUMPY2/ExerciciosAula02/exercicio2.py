import random
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np


dados={"Idade": [14, 17 ,18, 15, 15, 16, 17, 15, 16, 16, 15, 17, 15, 16, 
16, 18, 18, 19, 17, 16, 17, 15, 16, 17, 17, 19, 20, 18, 
17, 16, 15, 16, 16, 17, 18, 18, 17, 17, 15, 16, 16, 15]}

print(np.mean(dados['Idade']))

print(np.std(dados['Idade']))

df = pd.DataFrame(dados)


#BOXPLOT
df.boxplot(column=['Idade'], grid=False)
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
bp = ax.boxplot(df)
plt.show()

#HISTOGRAMA
fig = plt.figure()
bp = plt.hist(df)
plt.show()

#CURVA DA DISTRIBUIÇÃO
desvio = np.std(dados['Idade'], ddof=1)
media = np.mean(dados['Idade'])

dominio = np.linspace(np.min(dados['Idade']), np.max(dados['Idade']))
plt.plot(dominio, norm.pdf(dominio, media, desvio))
plt.show()