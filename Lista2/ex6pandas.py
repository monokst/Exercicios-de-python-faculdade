#Exercicio 6 | Ordenando a coluna Produto em orfem alfabetica

import pandas as pd

#criação do DataFrame
dados = {
    'Produto': ['geladeira', 'fone', 'carregador', 'monitor', 'roteador'],
    'Preço': [1500.00, None, 30.00, None, 240.00],
    'quantidade': [3, 2, 1, 2, 1],
}

df = pd.DataFrame(dados)

#ordenando pela coluna Produto em ordem alfabética
df_ordenado = df.sort_values(by='Produto')

print(df_ordenado)