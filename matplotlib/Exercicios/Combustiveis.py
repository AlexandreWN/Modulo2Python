import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('./Docs/combustiveis.csv')

def calculate_percentage(val, total):
    percent = float(val / total)
    beautiful_percent = ("%.2f" % (percent * 100) + "%")
    return percent * 100

total = df.PRODUTO.count()

ETANOLHIDRATADO = (df["PRODUTO"] == "ETANOL HIDRATADO").sum()
OLEODIESEL = (df["PRODUTO"] == "ÓLEO DIESEL").sum()
OLEODIESELS10 = (df["PRODUTO"] == "ÓLEO DIESEL S10").sum()
GASOLINACOMUM = (df["PRODUTO"] == "GASOLINA COMUM").sum()
GLP = (df["PRODUTO"] == "GLP").sum()
GNV = (df["PRODUTO"] == "GNV").sum()



ETANOLHIDRATADO = calculate_percentage(ETANOLHIDRATADO,total)
OLEODIESEL = calculate_percentage(OLEODIESEL,total)
OLEODIESELS10 = calculate_percentage(OLEODIESELS10,total)
GASOLINACOMUM = calculate_percentage(GASOLINACOMUM,total)
GLP = calculate_percentage(GLP,total)
GNV = calculate_percentage(GNV,total)

#Grafico
labels = ['ETANOL HIDRATADO','OLEO DIESEL','OLEO DIESEL S10','GASOLINA COMUM','GLP','GNV']
sizes = [ETANOLHIDRATADO, OLEODIESEL, OLEODIESELS10, GASOLINACOMUM, GLP, GNV]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
shadow=False, startangle=90)
ax1.axis('equal')
plt.show()
