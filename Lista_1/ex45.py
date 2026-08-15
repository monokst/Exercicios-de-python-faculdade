# Exercício 45 | Par ou Ímpar em Lista

numeros = [10, 8, 3, 7, 15] #lista de numero

for numero in numeros: #verifica se é par ou impar
    if numero % 2 == 0:
        print(numero, "é par")
    else:
        print(numero, "é ímpar")