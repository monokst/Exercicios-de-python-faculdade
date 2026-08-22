#Exercicio 4 | Desconto de 10% nos produtos

import pandas as pd

#criação do DataFrame
dados = {
    'Produto': ['geladeira', 'fone', 'carregador', 'monitor', 'roteador'],
    'Preço': [1500.00, 50.00, 30.00, 600.00, 240.00],
    'quantidade': [3, 2, 1, 2, 1],
}

df = pd.DataFrame(dados) #transforma em uma tabela com linhas e colunas

#criando a coluna desconto (10% sobre o valor do Preço)
df['Desconto'] = df['Preço'] * 0.10

print(df)