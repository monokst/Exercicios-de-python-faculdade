#Exercicio 12 | Verifique quais colunas de um DataFrame contêm valores duplicados.

import pandas as pd

# Criação do DataFrame
dados = {
    'Produto': ['geladeira', 'fone', 'fone', 'monitor', 'roteador'],
    'Preço': [1500.00, 50.00, 50.00, 600.00, 240.00],
    'Quantidade': [3, 2, 2, 2, 1]
}

df = pd.DataFrame(dados)

# Verificando valores duplicados em cada coluna
for coluna in df.columns:
    print(coluna, df[coluna].duplicated().any())