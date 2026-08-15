#Exercicio 28 | Gráfico de barras

import matplotlib.pyplot as plt

categorias = input("Digite as categorias separadas por vírgula").split(",") #o split, separa o que o usuário digitou pela vírgula.
valores = input ("Digite os valores separados por vírgula").split(",") 

#converte os valores para números
valores = [int(valor) for valor in valores]

#cria o grafico de barras
plt.bar(categorias, valores) #plt.bar() cria o grafico de barras.

#adiciona título e nomes aos eixos
plt.title("Gráfico de Barras") #titulo
plt.xlabel("Categorias") #categorias eixo x
plt.ylabel("Valores") #valores eixo y