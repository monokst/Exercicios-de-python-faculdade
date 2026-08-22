# Exercicio 11 | Crie um gráfico de barras empilhadas para três categorias com três grupos de valores

import matplotlib.pyplot as plt

# Definindo as três categorias do gráfico
categorias = ['Categoria A', 'Categoria B', 'Categoria C']

# Definindo os valores de cada grupo para cada categoria
grupo1 = [10, 20, 15]
grupo2 = [15, 10, 20]
grupo3 = [5, 15, 10]

# Criando as barras do primeiro grupo
plt.bar(categorias, grupo1, label='Grupo 1')

# Adicionando o segundo grupo sobre as barras do primeiro
plt.bar(categorias, grupo2, bottom=grupo1, label='Grupo 2')

# Calculando a posição onde o terceiro grupo começará
base_grupo3 = [
    grupo1[i] + grupo2[i]
    for i in range(len(categorias))
]

# Adicionando o terceiro grupo sobre os dois anteriores
plt.bar(
    categorias,
    grupo3,
    bottom=base_grupo3,
    label='Grupo 3'
)

# Adicionando título e identificando os eixos
plt.title('Gráfico de Barras Empilhadas')
plt.xlabel('Categorias')
plt.ylabel('Valores')

# Exibindo a legenda para identificar cada grupo
plt.legend()

# Exibindo o gráfico
plt.show()