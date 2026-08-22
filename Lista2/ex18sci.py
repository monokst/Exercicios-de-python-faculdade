#Exercicio 18 |Intepole valores

import numpy as np
from scipy.interpolate import CubicSpline

#define os valores conhecidos de x
x = np.array([1, 2, 3, 4, 5])

#define os valores de y usando y = x²
y = x**2

#cria uma interpolação usando uma spline cúbica
spline = CubicSpline(x, y)

print(spline(2.5))