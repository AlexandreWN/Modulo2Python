import pandas as pd

casa = pd.read_csv("./DocsProva/dados.csv", sep=",")

filtro = ((casa["quartos"] == 3) & (casa["area"] > 130) & (casa["bairro"] == "Tijuca"))

print(casa[filtro].sort_values(by='preco', na_position='first').head(1))
    