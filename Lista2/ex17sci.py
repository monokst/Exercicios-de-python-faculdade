#Exercicio 17 | Raiz cúbica de 27 utilizando SciPy

from scipy.optimize import root

#define a função
def f(x):
    return x**3 - 27

#procura a raiz começando pelo valor 2
resultado = root(f, 2)

print(resultado.x[0])