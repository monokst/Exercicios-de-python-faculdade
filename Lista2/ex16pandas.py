#Exercicio 16 | Crie um gráfico de barras a partir de um DataFrame usando a biblioteca Pandas

import pandas as pd
import matplotlib.pyplot as plt

# Criação do DataFrame
dados = {
    'Produto': ['geladeira', 'fone', 'carregador', 'monitor', 'roteador'],
    'Preço': [1500.00, 50.00, 30.00, 600.00, 240.00],
    'Quantidade': [3, 2, 1, 2, 1]
}

df = pd.DataFrame(dados)

# Criando o gráfico de barras
df.plot(
    x='Produto',
    y='Quantidade',
    kind='bar'
)

plt.title('Quantidade de Produtos')
plt.xlabel('Produto')
plt.ylabel('Quantidade')
plt.show()