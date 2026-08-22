#Exercicio 12

import numpy as np

matriz = np.eye(4)
matriz[np.diag_indices(4)] = 7 #pega a diagonal principal e altera os valores para 7

print(matriz)