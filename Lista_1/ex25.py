#Exercicio 25 | Classificação de Números

#cria uma lista contendo números
numeros = [10, -5, 0, 8, -3, 0, 15, -7]

#cria uma lista vazia
positivos = []
negativos = []
zeros = []

for numero in numeros:
    if numero > 0:
        positivos.append(numero) #adiciona o número à lista de positivos
    elif numero < 0:
        negativos.append(numero) #adiciona o número à lista de negativos
    else:
        zeros.append(numero) #adiciona o zero à lista de zeros

print("Positivos:", positivos)
print("Negativos:", negativos)
print("Zeros:", zeros)