# Exercicio 10 | Integral dupla: f(x,y) = xy + x² x no intervalo [0,1] e y em [0,2]
from scipy.integrate import dblquad

# Define a função que será integrada, a ordem dos argumentos é y, x para o dblquad
def f(y, x):
    return x*y + x**2

# Calcula a integral dupla
# x varia de 0 até 2
# y varia de 0 até 1
resultado, _ = dblquad(
    f,
    0, 2,
    lambda x: 0,
    lambda x: 1
)

print(resultado)