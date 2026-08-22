# Exercicio 6 | Plote dois gráficos de linha em subplots diferentes: y₁ = eˣ e y₂ = log(x)

import matplotlib.pyplot as plt
import numpy as np

# Valores de x
x = np.linspace(0.1, 5, 100)

# Funções
y1 = np.exp(x)
y2 = np.log(x)

# Criando os subplots
fig, ax = plt.subplots(1, 2)

# Primeiro gráfico
ax[0].plot(x, y1)
ax[0].set_title('y = eˣ')
ax[0].set_xlabel('x')
ax[0].set_ylabel('y')

# Segundo gráfico
ax[1].plot(x, y2)
ax[1].set_title('y = log(x)')
ax[1].set_xlabel('x')
ax[1].set_ylabel('y')

plt.show()