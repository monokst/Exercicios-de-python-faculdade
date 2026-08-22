# Exercicio 9 | Adicione título, rótulos e uma grade personalizada a um gráfico de linha

import matplotlib.pyplot as plt

# Definindo os valores dos eixos x e y
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Criando o gráfico de linha a partir dos valores de x e y
plt.plot(x, y)

# Adicionando o título e os nomes dos eixos do gráfico
plt.title('Gráfico de Linha')
plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')

# Adicionando uma grade personalizada com linhas tracejadas
plt.grid(
    True,
    linestyle='--',
    linewidth=0.5
)

# Exibindo o gráfico
plt.show()