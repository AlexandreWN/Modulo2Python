import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('./Docs/respiradores.csv')

estados_sul = df.loc[:,['PARANA','SANTA CATARINA','RIO GRANDE DO SUL ']]

print(estados_sul.sum())
def valor():
    x=estados_sul.sum()["PARANA"]
    y=estados_sul.sum()["SANTA CATARINA"]
    z=estados_sul.sum()["RIO GRANDE DO SUL "]
    return x,y,z
sizes=valor()

p, tx, autotexts = plt.pie(estados_sul.sum(), labels=estados_sul.columns, 
        autopct="", shadow=True)
print(autotexts)
for i, a in enumerate(autotexts):
    a.set_text("{}".format(sizes[i]))

plt.title('COMPRA DE RESPIRADORES NO SUL')
plt.show()


#multiplas barras
print(df.shape)
print([a-0.25 for a in range(df.shape[0])])
print([a+0.25 for a in range(df.shape[0])])
print(df.PARANA)
    
plt.bar([i-0.25 for i in range(df.shape[0])],df.PARANA, width = +0.25,
        label = 'Paraná', align = 'edge')

plt.bar([a+0.25 for a in range(df.shape[0])],df.TOTAL/30,width = -0.25,
       label = 'Média brasileira', align = 'edge')
plt.legend()
plt.grid(color='lightgray',linestyle='dashed')

plt.show()


plt.bar([a-0.25 for a in range(df.shape[0])],df.PARANA, width = 0.25,
        label = 'Paraná', align = 'edge')
plt.bar([a+0.25 for a in range(df.shape[0])],df.TOTAL/30,width = -0.25,
       label = 'Média brasileira', align = 'edge')
plt.xticks(np.arange(11),df.MES, rotation=45)
plt.legend()
plt.grid(color='lightgray',linestyle='dashed')

plt.show()