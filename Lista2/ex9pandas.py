#Exercicio 9 | Exporte o DataFrame resultante para um arquivo CSV chamado resultados.csv.

import pandas as pd

# Criação do DataFrame
dados = {
    'Produto': ['geladeira', 'fone', 'carregador', 'monitor', 'roteador'],
    'Preço': [1500.00, 50.00, 30.00, 600.00, 240.00],
    'Quantidade': [3, 2, 1, 2, 1],
    'Categoria': ['Eletrodoméstico', 'Acessório', 'Acessório', 'Eletrônico', 'Eletrônico']
}

df = pd.DataFrame(dados)

# Exportando para CSV
df.to_csv('resultados.csv', index=False)

print('Arquivo exportado com sucesso!')