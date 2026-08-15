# Exercício 38 | Contar Palavras em Texto

texto = input("Digite um texto: ")

#separa o texto em palavras
palavras = texto.split()

#conta as palavras
quantidade = len(palavras) #o len conta a quantidade de objetos

print("Quantidade de palavras:", quantidade)