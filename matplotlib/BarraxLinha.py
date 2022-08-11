import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./Docs/respiradores.csv')

x=df.MES
altura=df.TOTAL
plt.bar(x,altura, 1.5,align= "center", edgecolor="black" )
plt.title("COMPRA DE RESPIRADORES POR MÊS")
plt.xticks(rotation = '90')
plt.yticks(rotation = '45')
plt.show()

total_por_estado = df.sum()[1:-1]
print(total_por_estado)

x=df.columns[1:-1]
plt.barh(x, total_por_estado, color = 'black', zorder=3)
plt.title('COMPRA DE RESPIRADORES POR ESTADO')
plt.xticks(rotation='vertical')
plt.grid(zorder=0)
plt.show()

plt.plot(df.MES,df.PARANA)
plt.xticks(rotation='45')
plt.grid(linestyle='dashed')
plt.title("COMPRA DE RESPIRADORES POR MÊS NO PARANÁ")
plt.show()

plt.plot(df.MES,df.PARANA,marker='o', label = 'Paraná')
plt.plot(df.MES,df['SÃO PAULO'],marker='o', label = 'São Paulo')
plt.plot(df.MES,df['SANTA CATARINA'],marker='o', label = 'Santa Catarina')
plt.legend()
plt.xticks(rotation='45')
plt.grid(linestyle='dashed')
plt.show()

plt.scatter(df['MES'],df['PARANA'], label = 'Paraná')
plt.scatter(df['MES'],df['SANTA CATARINA'], label = 'Santa Catarina')
plt.scatter(df['MES'],df['GOIAS'], label = 'Goiás')
plt.scatter(df['MES'],df['PERNAMBUCO'], label = 'Pernambuco')
plt.scatter(df['MES'],df['AMAPA'], label = 'Amapá')
plt.legend() #fontsize=10 / prop={"size":10}
plt.title("")
plt.xticks(rotation=45)
plt.show()


fig, eixo = plt.subplots(nrows = 2, ncols = 2, figsize = (20,20))
eixo[0][0].bar(df.MES,df.TOTAL)
eixo[0][1].bar(df.columns[1:-1],df.sum()[1:-1])
eixo[1][0].scatter(df['MES'],df['GOIAS'], label = 'Goiás')
eixo[1][1].plot(df.MES,df.PARANA, color = 'purple', marker='x', linewidth = 3, markersize=10)

eixo[0][0].set_title("Oi")
eixo[0][0].set_ylabel("Ola")

eixo[0][0].tick_params(axis='x',  labelrotation=45) # os métodos dos eixos de subplots são diferentes das funções do plot
eixo[0][1].tick_params(axis='x', labelrotation=90)
eixo[1][0].tick_params(axis='x', labelrotation=45) # os métodos dos eixos de subplots são diferentes das funções do plot
eixo[1][1].tick_params(axis='x', labelrotation=90)


plt.show()