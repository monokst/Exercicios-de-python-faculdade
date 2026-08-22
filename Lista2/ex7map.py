# Exercicio 7 | Crie um gráfico de dispersão com tamanho dos pontos variando de acordo com os valores de y

import matplotlib.pyplot as plt
import numpy as np

# Gerando os dados
x = np.random.rand(100)
y = np.random.rand(100)

# Tamanho dos pontos baseado em y
tamanho = y * 500

# Criando o gráfico
plt.scatter(x, y, s=tamanho)

plt.title('Dispersão com Tamanho Variável')
plt.xlabel('x')
plt.ylabel('y')

plt.show()