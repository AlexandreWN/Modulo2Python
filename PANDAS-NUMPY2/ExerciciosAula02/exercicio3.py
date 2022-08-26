import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

dados = {'Area':[40,45,50,53,60,65,100,110,113,130],
'Valor':[120,180,190,187,195,200,300,320,305,400]}

dados = pd.DataFrame(data=dados)

X = dados['Area'].values
Y = dados['Valor'].values

X = X.reshape(-1, 1)

regressor = LinearRegression()

regressor.fit(X, Y)

plt.scatter(X, Y)

plt.plot(X, regressor.predict(X), color='red')

plt.title("Regressão linear simples")
plt.xlabel('Idade')
plt.ylabel('Valor do plano de saúde')

plt.show()

#BOXPLOT
dados.boxplot(column=['Area', 'Valor'], grid=False)
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
bp = ax.boxplot(dados)
plt.show()

idade = np.array(57)
previsao1 = regressor.predict(idade.reshape(-1,1))
previsao2 = regressor.intercept_ + regressor.coef_*idade

print(previsao1)
print(previsao2)
