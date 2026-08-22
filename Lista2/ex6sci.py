# Exercicio 6 | Matriz inversa 5x5 de números aleatórios
import numpy as np
from scipy.linalg import inv

#cria uma matriz aleatória de tamanho 5x5
matriz = np.random.rand(5, 5)

#calcula a matriz inversa
resultado = inv(matriz)

print(resultado)