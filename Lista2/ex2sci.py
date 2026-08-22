# Exercicio 2 | dy/dx = x - y, com y(0)=1, no intervalo [0, 10]

import numpy as np
from scipy.integrate import solve_ivp

#define a equação diferencial dy/dx = x - y
def f(x, y):
    return x - y

#resolve a equação diferencial no intervalo de 0 até 10
#a condição inicial é y(0) = 1
#t_eval define 100 pontos onde a solução será calculada
solucao = solve_ivp(
    f,
    [0, 10],
    [1],
    t_eval=np.linspace(0, 10, 100)
)

print(solucao.y[0])