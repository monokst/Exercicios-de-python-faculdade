# Exercicio 7 | Interpolação cúbica

import numpy as np
from scipy.interpolate import interp1d

#define os valores conhecidos de x
x = np.array([0, 1, 2, 3, 4])

#define os valores conhecidos de y
y = np.array([0, 2, 3, 5, 4])

#cria uma função de interpolação cúbica
interpolacao = interp1d(x, y, kind="cubic")

#estima o valor de y para x = 2.5
print(interpolacao(2.5))