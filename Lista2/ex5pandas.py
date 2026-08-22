#Exercicio 5 | Remover linhas com valores nulos

import pandas as pd

#criação do DataFrame
dados = {
    'Produto': ['geladeira', 'fone', 'carregador', 'monitor', 'roteador'],
    'Preço': [1500.00, None, 30.00, None, 240.00],
    'quantidade': [3, 2, 1, 2, 1],
}

df = pd.DataFrame(dados) #transforma em uma tabela com linhas e colunas

df_sem_nulos = df.dropna() #vai remover os valores nulos

print(df_sem_nulos)