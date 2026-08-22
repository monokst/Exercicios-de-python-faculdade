# Exercicio 9 | Ajuste de curva quadrática aos pontos (1,2), (2,4), (3,5), (4,7), (5,8)

import numpy as np
from scipy.optimize import curve_fit

#array com dados
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 7, 8])

#define uma função quadrática com três parâmetros
def f(x, a, b, c):
    return a*x**2 + b*x + c

#encontra os valores de a, b e c que melhor ajustam os dados
parametros, _ = curve_fit(f, x, y)

print(parametros)