# Exercicio 3 | Raízes de f(x) = x⁴ - 3x³ + 2
from scipy.optimize import root

#define a função cuja raiz queremos encontrar
def f(x):
    return x**4 - 3*x**3 + 2

#testa diferentes valores iniciais para procurar as raízes
for chute in [-2, -1, 0, 1, 2, 3]:
    resultado = root(f, chute)

#verifica se o método conseguiu encontrar uma solução
    if resultado.success:
        print(resultado.x[0])