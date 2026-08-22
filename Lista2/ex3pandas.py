#Exercicio 3 | Filtrar valores maiores de 100 na coluna Preco

import pandas as pd

# tabela com dados 
dados = {
    'Produto': ['geladeira', 'fone', 'carregador', 'monitor', 'roteador'],
    'Preço': [1500.00, 50.00, 30.00, 600.00, 240.00],
    'quantidade': [3, 2, 1, 2, 1],
}

# convertendo o dicionário para um DataFrame do Pandas
df = pd.DataFrame(dados)

#filtragem (igual ao exemplo do professor)
filtrar_dados = df[df['Preço'] > 100]
print(filtrar_dados)