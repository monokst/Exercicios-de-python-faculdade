#Exercicio 12 | Contagem de Caracteres
texto = input("Digite uma palavra ou frase: ")

for letra in texto:
    print(letra, "aparece", texto.count(letra), "vezes")