#Exercicio 7 | Crie uma nova coluna chamada Total que seja o produto entre as colunas Preço e Quantidade.

import pandas as pd

# Criação do DataFrame
dados = {
    'Produto': ['geladeira', 'fone', 'carregador', 'monitor', 'roteador'],
    'Preço': [1500.00, 50.00, 30.00, 600.00, 240.00],
    'Quantidade': [3, 2, 1, 2, 1],
    'Categoria': ['Eletrodoméstico', 'Acessório', 'Acessório', 'Eletrônico', 'Eletrônico']
}

df = pd.DataFrame(dados)

# Criando a coluna Total
df['Total'] = df['Preço'] * df['Quantidade']

print(df)