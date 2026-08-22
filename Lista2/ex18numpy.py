#Exercicio 18

import numpy as np

# Cria um array com 10 números inteiros aleatórios entre 1 e 100
array = np.random.randint(1, 101, 10)

# Verifica quais valores são múltiplos de 5
# O operador % calcula o resto da divisão
# Se o resto for 0, significa que o número é múltiplo de 5
array[array % 5 == 0] = 0

print(array)