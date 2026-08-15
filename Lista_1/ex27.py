#Exercicio 27 | Anagramas

palavra1 = input("Digite a primeira palavra: ").lower() #o lower vai deixar todas as letras minusculas, assim se tiver um "A" e "a" serão considerados iguais
palavra2 = input("Digite a segunda palavra: ").lower()

if sorted(palavra1) == sorted(palavra2): #compara as letras das duas palavras
    print("São anagramas")
else:
    print("Não são anagramas")