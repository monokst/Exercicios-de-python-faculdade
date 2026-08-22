# 20. Sistema de equações lineares com três variáveis
import numpy as np
from scipy.linalg import solve

#define a matriz dos coeficientes
A = np.array([
    [1, 1, 1],
    [2, -1, 1],
    [1, 2, -1]
])

#define os valores do lado direito das equações
b = np.array([6, 3, 2])

#resolve o sistema linear A*x = b
resultado = solve(A, b)

print(resultado)