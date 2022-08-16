import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

tips = pd.read_csv('../Docs/tips.csv',sep=';')
print(tips.head())
print(tips.shape)

sns.relplot(x='total_bill', y='tip', data = tips)
plt.show()