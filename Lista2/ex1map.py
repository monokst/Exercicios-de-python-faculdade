# Exercicio 1 | Crie um gráfico de linha para a função y = x³ no intervalo de x = -10 até x = 10

import matplotlib.pyplot as plt
import numpy as np

# Valores de x
x = np.linspace(-10, 10, 100)

# Função y = x³
y = x**3

# Criando o gráfico
plt.plot(x, y)

plt.title('Gráfico de y = x³')
plt.xlabel('x') #mostra x
plt.ylabel('y') #mostra y
plt.grid()

plt.show()