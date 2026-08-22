#Exercicio 7

import numpy as np

# Cria dois arrays com 10 números aleatórios
array1 = np.random.rand(10)
array2 = np.random.rand(10)

print("Array 1:")
print(array1)

print("\nArray 2:")
print(array2)

# Calcula a matriz de correlação
correlacao = np.corrcoef(array1, array2)

print("\nMatriz de correlação:")
print(correlacao)

# Mostra apenas a correlação entre os dois arrays
print("\nCorrelação entre os arrays:", correlacao[0, 1])