#Exercicio 10 | Leia um arquivo CSV, renomeie as colunas e exiba as 5 últimas linhas do DataFrame

import pandas as pd

# Ler o arquivo CSV
df = pd.read_csv("/content/produtos.csv", encoding="latin1", sep=";")

# Renomear as colunas
df = df.rename(columns={
    'Produto': 'Nome',
    'Preço': 'Valor',
    'Quantidade': 'Qtd',
    'Categoria': 'Tipo'
})

# Exibir as 5 últimas linhas
print(df.tail(5))