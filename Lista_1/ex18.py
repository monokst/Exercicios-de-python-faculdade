#Exercicio 18 | Numero primo

numero = int(input("Escreva um número: "))

# Variável que vai contar quantos divisores o número possui
divisores = 0

# Percorre todos os números de 1 até o número informado
for i in range(1, numero + 1):

    # Verifica se o resto da divisão é 0
    # Se for, significa que i é um divisor de numero
    if numero % i == 0:
        divisores += 1  # Aumenta a quantidade de divisores em 1

# Um número primo possui exatamente 2 divisores: 1 e ele mesmo
if divisores == 2:
    print("É primo")
else:
    print("Não é primo")