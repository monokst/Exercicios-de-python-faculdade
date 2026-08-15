#Exercicio 17 | Dicionario de contagem de palavras

frase = (input("digite um frase: "))
palavras = frase.split() #separa a string com virgulas
contagem = {} #dicionario

for palavra in palavras: #percorre cada palavras
    if palavra in contagem: #verifica se está no dicionario
        contagem[palavra] += 1 # se tiver mais palavra repetida, ele vai contabilizando
    else:
        contagem[palavra] = 1 #se tiver só um palavra, ele coloca um

print(contagem)