#Exercicio 20 | Matriz Transposta

#cria uma matriz
matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

#cria uma lista vazia
transposta = []

#percorre a quantidade de colunas da matriz
for i in range(len(matriz[0])):

    #cria uma nova linha vazia
    linha = []

    #percorre a quantidade de linhas da matriz
    for a in range(len(matriz)):

        #pega os elementos da coluna da matriz original e adiciona na nova linha
        linha.append(matriz[a][i])

    #adiciona a nova linha na matriz transposta
    transposta.append(linha)

print(transposta)