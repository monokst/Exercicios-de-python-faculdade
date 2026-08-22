# Exercicio 20 | Adicione uma grade com espaçamento personalizado a um gráfico de linha para y = x²

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

# Valores de x
x = np.linspace(-10, 10, 100)

# Função y = x²
y = x**2

# Criando o gráfico
plt.plot(x, y)

# Título e rótulos
plt.title('Função y = x²')
plt.xlabel('X')
plt.ylabel('Y')

# Definindo o espaçamento da grade
plt.gca().xaxis.set_major_locator(MultipleLocator(2))
plt.gca().yaxis.set_major_locator(MultipleLocator(20))

# Adicionando a grade
plt.grid()

plt.show()