#Exercicio 17 | Adicione uma coluna ao DataFrame que calcule o imposto (5%) sobre o valor da coluna Total

import pandas as pd

# Criação do DataFrame
dados = {
    'Produto': ['geladeira', 'fone', 'carregador', 'monitor', 'roteador'],
    'Preço': [1500.00, 50.00, 30.00, 600.00, 240.00],
    'Quantidade': [3, 2, 1, 2, 1]
}

df = pd.DataFrame(dados)

# Criando a coluna Total
df['Total'] = df['Preço'] * df['Quantidade']

# Calculando o imposto de 5%
df['Imposto'] = df['Total'] * 0.05

print(df)