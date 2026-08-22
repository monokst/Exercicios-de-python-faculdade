#Exercicio 18 | Exiba apenas as linhas de um DataFrame onde o nome do produto começa com a letra "B"

import pandas as pd

# Criação do DataFrame
dados = {
    'Produto': ['geladeira', 'fone', 'carregador', 'monitor', 'roteador', 'bateria'],
    'Preço': [1500.00, 50.00, 30.00, 600.00, 240.00, 100.00],
    'Quantidade': [3, 2, 1, 2, 1, 2],
    'Categoria': ['Eletrodoméstico', 'Acessório', 'Acessório', 'Eletrônico', 'Eletrônico', 'Acessório']
}

df = pd.DataFrame(dados)

# Exibir produtos que começam com a letra B
resultado = df[df['Produto'].str.lower().str.startswith('b')]

print(resultado)