# Exercicio 14 | Crie um gráfico de barras horizontal para 4 categorias com valores gerados aleatoriamente

import matplotlib.pyplot as plt
import numpy as np

# Definindo as quatro categorias do gráfico
categorias = ['A', 'B', 'C', 'D']

# Gerando quatro valores aleatórios entre 10 e 100
valores = np.random.randint(10, 100, 4)

# Criando o gráfico de barras na horizontal
plt.barh(categorias, valores)

# Adicionando título e identificando os eixos
plt.title('Gráfico de Barras Horizontal')
plt.xlabel('Valores')
plt.ylabel('Categorias')

# Exibindo o gráfico
plt.show()