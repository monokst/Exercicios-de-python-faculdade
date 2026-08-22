# Exercicio 8 | Sistema:  3x + 2y = 5 e x + 4y = 6
import numpy as np
from scipy.linalg import solve

#define a matriz dos coeficientes do sistema
A = np.array([
    [3, 2],
    [1, -4]
])

#define os valores do lado direito das equações
b = np.array([5, 6])

#resolve o sistema linear A*x = b
resultado = solve(A, b)

print(resultado)