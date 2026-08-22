#Exercicio 6
import numpy as np

matriz = np.eye(5,5) #matriz

soma_colunas = np.sum(matriz, axis=0) #o axis=0 vai somar cada coluna, se fosse linha coloca 1

print("A matriz é ", matriz)

print("A soma das colunas é ", soma_colunas)