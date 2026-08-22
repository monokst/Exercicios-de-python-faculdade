#Exercicio 14

import numpy as np

# Cria o primeiro array com 10 números aleatórios
array1 = np.random.randint(1, 20, 10)

# Cria o segundo array com 10 números aleatórios
array2 = np.random.randint(1, 20, 10)

# Calcula a diferença entre os elementos dos dois arrays
diferenca = array1 - array2

# Calcula a média das diferenças
media = np.mean(diferenca)

print("Array 1:", array1)

print("Array 2:", array2)

print("Diferenças:", diferenca)

print("Média das diferenças:", media)