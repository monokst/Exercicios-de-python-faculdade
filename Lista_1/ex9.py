#Exercicio 9 | Fatorial de numero
num2 = int(input("digite um número: "))
fatorial = 1 #fatorial vai ter o valor de 1
for i in range (1, num2 + 1): #se o usuario escreve 5, vai virar range(1, 6)
  fatorial = fatorial * i #vai multiplicar o fatorial com a quantidade que foi digitada

print(f"O fatorial de {num2} é {fatorial}")