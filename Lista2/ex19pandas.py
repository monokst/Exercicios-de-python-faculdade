#Exercicio 19 | Crie um DataFrame a partir de um dicionário de listas e calcule a média de cada coluna numérica

import pandas as pd

# Criação do DataFrame
dados = {
    'Produto': ['geladeira', 'fone', 'carregador', 'monitor', 'roteador'],
    'Preço': [1500.00, 50.00, 30.00, 600.00, 240.00],
    'Quantidade': [3, 2, 1, 2, 1]
}

df = pd.DataFrame(dados)

# Calculando a média das colunas numéricas
media = df.mean(numeric_only=True)

print(media)