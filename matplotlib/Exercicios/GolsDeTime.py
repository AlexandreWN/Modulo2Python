import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('./Docs/gols_pr.csv')

Coritiba = (df["clube"] == "coritiba")
Coritibax = (df[Coritiba]["gols_pro"])
y = (df["ano"].unique())

athletico = (df["clube"] == "athletico-pr")
athleticox = (df[athletico]["gols_pro"])

parana = (df["clube"] == "parana")
paranax = (df[parana]["gols_pro"])

plt.plot(y,Coritibax)
plt.plot(y,athleticox)
plt.plot(y,paranax)
plt.title("COMPRA DE RESPIRADORES TOTAL POR REGIÃO")
plt.xticks(rotation = '90')
plt.yticks(rotation = '45')
plt.show()