#Exercicio 15 | Crie um DataFrame com dados faltantes e use a interpolação linear para preenchê-los

import pandas as pd

# Criação do DataFrame
dados = {
    'Produto': ['geladeira', 'fone', 'carregador', 'monitor', 'roteador'],
    'Preço': [1500.00, None, 30.00, None, 240.00]
}

df = pd.DataFrame(dados)

# Preenchendo os valores faltantes
df['Preço'] = df['Preço'].interpolate()

print(df)