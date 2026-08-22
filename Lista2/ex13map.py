# Exercicio 13 | Gere um gráfico de dispersão 3D para 100 pontos aleatórios utilizando Matplotlib

import matplotlib.pyplot as plt
import numpy as np

# Gerando os dados
x = np.random.rand(100)
y = np.random.rand(100)
z = np.random.rand(100)

# Criando o gráfico 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x, y, z)

ax.set_title('Gráfico de Dispersão 3D')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()