#Exercicio 2 | Leia um arquivo excel chamado vendas.xlsx

import pandas as pd

df = pd.read_excel("/content/vendas.xlsx")

print(df.head(10))