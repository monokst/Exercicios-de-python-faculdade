# Exercicio 1 | Calcule a integral de f(x)=x sin(x) no intervalo de 0 a π

import numpy as np
from scipy.integrate import quad

#define a função que será integrada
def f(x):
    return x**2 * np.sin(x) 

resultado, _ = quad(f, 0, np.pi) #calcula a integral da função no intervalo de 0 até pi

print(resultado)