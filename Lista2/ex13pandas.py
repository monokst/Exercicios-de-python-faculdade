#Exercicio 13 | Crie uma tabela dinâmica a partir do DataFrame, calculando a soma de Quantidade por Categoria

import pandas as pd

# Criação do DataFrame
dados = {
    'Produto': ['geladeira', 'fone', 'carregador', 'monitor', 'roteador'],
    'Preço': [1500.00, 50.00, 30.00, 600.00, 240.00],
    'Quantidade': [3, 2, 1, 2, 1],
    'Categoria': ['Eletrodoméstico', 'Acessório', 'Acessório', 'Eletrônico', 'Eletrônico']
}

df = pd.DataFrame(dados)

# Criando a tabela dinâmica
tabela = pd.pivot_table(
    df,
    values='Quantidade',
    index='Categoria',
    aggfunc='sum'
)

print(tabela)