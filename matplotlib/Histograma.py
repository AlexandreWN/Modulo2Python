import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./Docs/respiradores.csv')

totalPorEstado = df.iloc[:,1:-1].sum()

print(totalPorEstado)

plt.hist(totalPorEstado, ec="black", color="yellow")

plt.show()


#Duplo eixo
fig, eixo = plt.subplots(ncols=1,nrows=1,figsize=(10,5))
eixo.plot(df.MES,df.PARANA,label='Paraná', color='darkblue')

eixo2 = eixo.twinx()
eixo2.plot(df.MES,df.TOTAL/30,color='red')

eixo2.tick_params(axis='y', labelcolor='red')
eixo.tick_params(axis='y', labelcolor='darkblue')

eixo.set_ylabel("Paraná", color='darkblue',fontsize=15)
eixo2.set_ylabel("Média brasileira", color='red',fontsize=15)

eixo.grid(color='lightblue')
eixo2.grid(color='pink')

eixo.set_title('Compra de respiradores PARANÁ X Média brasileira', fontsize= 15)

plt.show()

fig.savefig('grafico_parana.png')