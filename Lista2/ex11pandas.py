#Exercicio 11 | Preencha os valores nulos de uma coluna numérica com a mediana dessa coluna.

import pandas as pd

# Criação do DataFrame
dados = {
    'Produto': ['geladeira', 'fone', 'carregador', 'monitor', 'roteador'],
    'Preço': [1500.00, 50.00, None, 600.00, 240.00],
    'Quantidade': [3, 2, 1, 2, 1]
}

df = pd.DataFrame(dados)

# Preenchendo o valor nulo com a mediana
df['Preço'] = df['Preço'].fillna(df['Preço'].median())

print(df)