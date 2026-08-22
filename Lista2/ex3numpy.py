#Exercicio 3

import numpy as np

array = np.zeros(15) #faz um array com 15 numeros com valor 0
array("antes da substituição", array)

array[4:10] = 1 # No Python, o índice começa em 0
print("Depois da substituição", array)