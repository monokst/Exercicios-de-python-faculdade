# Exercicio 13 | Determinante de matriz 6x6 aleatória entre -10 e 10
import numpy as np
from scipy.linalg import det

# Cria uma matriz aleatória 6x6, os valores ficam entre -10 e 10
matriz = np.random.uniform(-10, 10, (6, 6))

#calcula o determinante da matriz
resultado = det(matriz)

print(resultado)