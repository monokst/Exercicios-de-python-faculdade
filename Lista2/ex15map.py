# Exercicio 15 | Plote a função y = 1/x com x variando de 1 a 100

import matplotlib.pyplot as plt
import numpy as np

# Valores de x
x = np.arange(1, 101)

# o valor da Função
y = 1 / x

# Criando o gráfico
plt.plot(x, y)

plt.title('Função y = 1/x')
plt.xlabel('x')
plt.ylabel('y')

plt.show()