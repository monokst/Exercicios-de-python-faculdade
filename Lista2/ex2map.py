# Exercicio 2 | Plote um gráfico de dispersão para 100 pontos aleatórios com uma paleta de cores baseada nos valores de y

import matplotlib.pyplot as plt
import numpy as np

# Gera 100 pontos aleatórios
x = np.random.rand(100)
y = np.random.rand(100)

# Criando o gráfico
plt.scatter(x, y, c=y, cmap='viridis')

plt.title('Gráfico de Dispersão')
plt.xlabel('x')
plt.ylabel('y')
plt.colorbar(label='Valor de y')

plt.show()