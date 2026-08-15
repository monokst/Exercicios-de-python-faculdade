#Exercicio 19 | Jogo de adivinhação
#importa a biblioteca random para gerar números aleatórios
import random

numero = random.randint(1, 100) #gera um número aleatório entre 1 e 100

tentativa = int(input("Tente adivinhar o número: "))

while tentativa != numero: #continua repetindo enquanto o jogador não acertar

    if tentativa < numero:
        print("O número é maior!") #se a tentativa for menor que o número secreto
    else:
        print("O número é menor!") # caso contrário, a tentativa é maior que o número secreto

    tentativa = int(input("Tente novamente: "))  # pede uma nova tentativa

print("Parabéns! Você acertou!")