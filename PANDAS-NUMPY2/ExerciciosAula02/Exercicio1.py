import imp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dados = {'Mistura 1': [22.02, 23.83, 26.67, 25.38, 25.49, 23.50, 25.90, 24.89, 22.02,23.83],
         'Mistura 2': [21.49, 22.67, 24.62, 24.18, 22.78, 22.56, 24.46, 23.79, 22.02,22.02],
         'Mistura 3': [20.33, 21.67, 24.67, 22.45, 22.29, 21.95, 20.49, 21.81, 22.02,22.02]}


media1, media2, media3 = np.mean(dados['Mistura 1']), np.mean(dados['Mistura 2']), np.mean(dados['Mistura 3'])

mediana1, mediana2, mediana3 = np.median(dados['Mistura 1']), np.median(dados['Mistura 2']), np.median(dados['Mistura 3'])

desvio1, desvio2, desvio3 = np.std(dados['Mistura 1']), np.std(dados['Mistura 2']), np.std(dados['Mistura 3'])

df = pd.DataFrame(dados)
df.boxplot(column=["Mistura 1", "Mistura 2", "Mistura 3"], grid=False)

fig = plt.figure()

ax = fig.add_axes([0, 0, 1, 1])

bp = ax.boxplot(df)

plt.show()