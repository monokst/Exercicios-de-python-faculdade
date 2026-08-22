#Exercicio 19

import numpy as np

# Cria o primeiro array com 20 números inteiros aleatórios
array1 = np.random.randint(1, 11, 20)

# Cria o segundo array com 20 números inteiros aleatórios
array2 = np.random.randint(1, 11, 20)

# Calcula o produto escalar entre os dois arrays
produto_escalar = np.dot(array1, array2)

# Calcula o tamanho (norma) do primeiro array
norma1 = np.linalg.norm(array1)

# Calcula o tamanho (norma) do segundo array
norma2 = np.linalg.norm(array2)

# Calcula o cosseno do ângulo entre os arrays
cos_theta = produto_escalar / (norma1 * norma2)

# Calcula o ângulo em radianos
angulo_rad = np.arccos(cos_theta)

# Converte o ângulo de radianos para graus
angulo_graus = np.degrees(angulo_rad)

# Mostra os arrays
print("Array 1:", array1)
print("Array 2:", array2)

print("Ângulo:", angulo_graus, "graus")