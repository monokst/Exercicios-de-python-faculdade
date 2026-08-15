# Exercício 49 | Soma dos Dígitos
numero = input("Digite um valor:")
soma = 0

for digito in numero: #para cada digito dentro de numero
  soma += int (digito) #será somado

print(soma)