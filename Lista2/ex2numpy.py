#Exercicio 2

import numpy as np
matriz = np.arange(1,17).reshape(4,4) #arange serve colocar o intervalo de numeros especificos na tabela #o reshape serve para colocar o tamanho da matriz
ultimalinha = matriz[3] #pega o ultima linha da matriz

print(matriz)
print("a ultima linha da matriz é ", ultimalinha)