#Exercicio 14 | Mescle dois DataFrames baseados em uma coluna comum chamada ID utilizando um join

import pandas as pd

# Primeiro DataFrame
dados1 = {
    'ID': [1, 2, 3],
    'Produto': ['geladeira', 'fone', 'monitor']
}

df1 = pd.DataFrame(dados1)

# Segundo DataFrame
dados2 = {
    'ID': [1, 2, 3],
    'Preço': [1500.00, 50.00, 600.00]
}

df2 = pd.DataFrame(dados2)

# Fazendo o join
resultado = df1.merge(df2, on='ID', how='inner')

print(resultado)