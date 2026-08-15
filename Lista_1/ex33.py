# Exercicio 33 | Verificação de Anagramas

palavra1 = input("Digite a primeira palavra: ").lower() #o lower vai deixar todas as letras minusculas
palavra2 = input("Digite a segunda palavra: ").lower()

if sorted(palavra1) == sorted(palavra2): #compara as letras das duas palavras
    print("São anagramas")
else:
    print("Não são anagramas")