#Exercicio 20 | Agrupe os dados por uma coluna categórica e calcule a mediana de uma coluna numérica

import pandas as pd

# Criação do DataFrame
dados = {
    'Produto': ['geladeira', 'fone', 'carregador', 'monitor', 'roteador'],
    'Preço': [1500.00, 50.00, 30.00, 600.00, 240.00],
    'Quantidade': [3, 2, 1, 2, 1],
    'Categoria': ['Eletrodoméstico', 'Acessório', 'Acessório', 'Eletrônico', 'Eletrônico']
}

df = pd.DataFrame(dados)

# Agrupando por Categoria e calculando a mediana do Preço
resultado = df.groupby('Categoria')['Preço'].median()

print(resultado)