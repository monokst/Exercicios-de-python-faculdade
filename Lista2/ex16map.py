# Exercicio 16 | Crie um gráfico de linha com títulos para cada eixo e adicione um rótulo de texto no ponto x = 5

import matplotlib.pyplot as plt

# Dados
x = [1, 2, 3, 4, 5, 6, 7]
y = [2, 4, 6, 8, 10, 12, 14]

# Criando o gráfico
plt.plot(x, y)

plt.title('Gráfico de Linha')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Adicionando texto no ponto x = 5
plt.text(5, 10, 'Ponto x = 5')

plt.show()