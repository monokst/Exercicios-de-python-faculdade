# Exercício 34 | Contador de Vogais

palavra = input("Digite um texto: ").lower() #o lower vai deixar todas as letras minusculas

contador = 0 #conta desde o zero

#percorre cada letra do texto
for letra in palavra:
    if letra in "aeiou":
        contador += 1

print(f"Quantidade de vogais: {contador}")