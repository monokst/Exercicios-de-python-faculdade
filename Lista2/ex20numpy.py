#Exercicio 20

import numpy as np

# Cria uma matriz 4x4 com números inteiros aleatórios
matriz = np.random.randint(1, 100, (4, 4))

# Encontra o menor valor de cada linha
# axis=1 significa que a operação será feita por linha
menores = np.min(matriz, axis=1)

# Mostra a matriz
print("Matriz:")
print(matriz)

print("Menor valor de cada linha:", menores)