# Exercicio 16 | 
import numpy as np
from scipy.integrate import solve_ivp

#define o sistema de equações diferenciais
def f(x, y):
    return [y[1], -y[0]]

#resolve o sistema no intervalo de 0 até 10
#condições iniciais:
#posição = 1
#velocidade = 0
solucao = solve_ivp(
    f,
    [0, 10],
    [1, 0],
    t_eval=np.linspace(0, 10, 100)
)

print(solucao.y[0])