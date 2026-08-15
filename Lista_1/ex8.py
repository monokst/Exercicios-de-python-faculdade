#Exercicio 8 | Verificação de Palíndromo
palavra = input("digite uma palavra: ")

if palavra == palavra [::-1]: #inverte a palavra
  print("é um palindromo")
else:
  print("não é um palindromo")