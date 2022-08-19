import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

flights = pd.read_csv("./DocsProva/flights.csv", sep=",")

filtro = ((flights["year"] == 1950))

print(flights[filtro])

sns.barplot(x=flights[filtro]["passengers"], y=flights[filtro]["month"] ,data = flights[filtro])
plt.show()

