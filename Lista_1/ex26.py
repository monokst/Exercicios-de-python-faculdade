# Exercicio 26 | Calculadora Simples

# Entrada dos números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Entrada da operação
operacao = input("Digite a operação (+, -, *, /): ")

# Realiza a operação escolhida
if operacao == "+":
    resultado = numero1 + numero2
    print("Resultado:", resultado)

elif operacao == "-":
    resultado = numero1 - numero2
    print("Resultado:", resultado)

elif operacao == "*":
    resultado = numero1 * numero2
    print("Resultado:", resultado)

elif operacao == "/":
    # Verifica se o número não é zero antes de dividir
    if numero2 != 0:
        resultado = numero1 / numero2
        print("Resultado:", resultado)
    else:
        print("Não é possível dividir por zero.")

else:
    print("Operação inválida.")