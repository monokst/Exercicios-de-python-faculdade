# Exercicio 11 | Autovalores e autovetores de uma matriz 4x4 aleatória
import numpy as np
from scipy.linalg import eig


#cria uma matriz aleatória de tamanho 4x4
matriz = np.random.rand(4, 4)

#calcula os autovalores e autovetores da matriz
autovalores, autovetores = eig(matriz)

print(autovalores)
print(autovetores)