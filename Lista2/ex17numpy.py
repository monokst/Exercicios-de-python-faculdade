#Exercicio 17

import numpy as np

# Cria uma matriz 4x4 com números inteiros aleatórios
matriz = np.random.randint(1, 10, (4, 4))

# Cria as posições das linhas: 1, 2, 3 e 4
linhas = np.arange(1, 5).reshape(4, 1)

# Cria as posições das colunas: 1, 2, 3 e 4
colunas = np.arange(1, 5)

# Multiplica cada elemento pelo número da sua linha
# e pelo número da sua coluna
resultado = matriz * linhas * colunas

# Mostra a matriz original
print("Matriz original:")
print(matriz)

print("Resultado:")
print(resultado)