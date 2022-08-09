import pandas as pd

cars = pd.read_csv("./Docs/Cars93_miss.csv", sep=",")

cars = cars.loc[cars['Passengers'] == 5]

cars = cars.sort_values(by="MPG.city", ascending=False).sort_values(by="Price")

print(cars[["Manufacturer", "Make", "Price", "MPG.city", "Type", "Passengers"]].dropna().head(5))