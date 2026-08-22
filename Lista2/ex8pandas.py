#Exercicio 8 | Agrupe o DataFrame pela coluna Categoria e calcule o total de produtos por categoria.

import pandas as pd

# Criação do DataFrame
dados = {
    'Produto': ['geladeira', 'fone', 'carregador', 'monitor', 'roteador'],
    'Preço': [1500.00, 50.00, 30.00, 600.00, 240.00],
    'Quantidade': [3, 2, 1, 2, 1],
    'Categoria': ['Eletrodoméstico', 'Acessório', 'Acessório', 'Eletrônico', 'Eletrônico']
}

df = pd.DataFrame(dados)

# Agrupando por categoria e somando as quantidades
resultado = df.groupby('Categoria')['Quantidade'].sum()

print(resultado)