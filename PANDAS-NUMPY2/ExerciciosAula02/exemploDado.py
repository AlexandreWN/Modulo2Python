import random
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

lista = [random.randint(1,6) for i in range(200)]
dados = pd.DataFrame(data=lista, columns=['Densidade'])

fig = plt.figure()
bp = plt.hist(dados)
plt.show()

desvio = np.std(dados['Densidade'], ddof=1)
media = np.mean(dados['Densidade'])

dominio = np.linspace(np.min(dados['Densidade']), np.max(dados['Densidade']))
plt.plot(dominio, norm.pdf(dominio, media, desvio))
plt.show()
