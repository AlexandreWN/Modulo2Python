from ctypes import pointer
import pandas as pd
import matplotlib.pyplot as plt

flights = pd.read_csv("./DocsProva/flights.csv", sep=",")

filtro = ((flights["month"] == "May"))

print(flights[filtro])

labels = flights[filtro]["passengers"]
sizes = flights[filtro]["year"]
fig1, ax1 = plt.subplots()
ax1.plot(sizes, labels, color='green', marker='o',  mec='k', mfc='k')
plt.title("Passageiros de avião")
plt.legend()
plt.xticks(sizes)
plt.grid(linestyle='solid')
plt.show()