#Exercicio 10

import numpy as np

matriz = np.eye(6) # a diagonal principal recebe 1 e o restante recebe 0
matriz[np.diag_indices(6)] = np.arange(1, 7) #pega a diagonal principal e altera os valores crescente de 1 a 7


print(matriz)