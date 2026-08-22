#Exercicio 5

import numpy as np
array = np.random.randint(1,101,20)
print("antes da substituição", array)

# Substitui os valores múltiplos de 3 por -3
array[array % 3 == 0] = -3

print("Depois da substituição", array)