# Exercicio 14 | Minimizar: f(x,y) = (x-2)² + (y-3)²
from scipy.optimize import minimize

#define a função que será minimizada
def f(valores):
    x, y = valores
    return (x - 2)**2 + (y - 3)**2

#procura o ponto de mínimo começando em (0, 0)
resultado = minimize(f, [0, 0])

print(resultado.x)