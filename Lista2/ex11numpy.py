#Exercicio 11

import numpy as np

array = np.random.randint(1,101,101)

# Encontra os valores únicos e a quantidade de vezes que aparecem
valores, quantidades = np.unique(array, return_counts=True)

# Encontra a maior quantidade de repetições
maior_quantidade = np.max(quantidades)

# Encontra a moda
moda = valores[quantidades == maior_quantidade]

print(array)
print("\n o numero da moda é ", moda)