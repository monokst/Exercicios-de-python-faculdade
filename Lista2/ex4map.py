# Exercicio 4 | Crie um gráfico de barras para 5 categorias com valores diferentes, colorindo cada barra de uma cor diferente

import matplotlib.pyplot as plt

# Dados
categorias = ['A', 'B', 'C', 'D', 'E']
valores = [10, 25, 15, 30, 20]

# Criando o gráfico
plt.bar(
    categorias,
    valores,
    color=['red', 'blue', 'green', 'orange', 'purple']
)

plt.title('Valores por Categoria')
plt.xlabel('Categoria')
plt.ylabel('Valor')

plt.show()