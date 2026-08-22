#Exercicio 15

import numpy as np

# Cria um array com 20 números aleatórios
# Os números vão de 1 até 100
array = np.random.randint(1, 101, 20)

# Encontra os valores maiores que 50
# E substitui esses valores por 50
array[array > 50] = 50

print(array)