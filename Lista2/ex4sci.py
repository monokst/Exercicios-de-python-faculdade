#Exercicio 4 | Maximizar f(x) = -x² + 4x + 1
# minimize_scalar trabalha com minimização, então minimizamos -f(x)
from scipy.optimize import minimize

#define a função que será minimizada
def f(x):
    return -x[0]**2 + 4*x[0] + 1

#procura o ponto de mínimo começando pelo valor inicial 0
resultado = minimize(f, [0])

print(resultado.x)