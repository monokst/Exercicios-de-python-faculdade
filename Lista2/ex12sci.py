# Exercicio 12 | Resolver e^x - x² = 0, raiz mais próxima de x=1 REVISAR
import numpy as np
from scipy.optimize import root

#define a função cuja raiz será encontrada
def f(x):
    return np.exp(x) - x**2

#procura uma raiz começando pelo valor inicial 1
resultado = root(f, 1)

print(resultado.x[0])