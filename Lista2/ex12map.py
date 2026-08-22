# Exercicio 12 | Plote um gráfico de linha com uma função quadrática e ajuste os limites do eixo para focar nos valores x = -5 a x = 5

import matplotlib.pyplot as plt
import numpy as np

# Valores de x
x = np.linspace(-10, 10, 100)

# Função quadrática
y = x**2

# Criando o gráfico
plt.plot(x, y)

# Limitando o eixo x
plt.xlim(-5, 5)

plt.title('Função Quadrática')
plt.xlabel('x')
plt.ylabel('y')

plt.show()