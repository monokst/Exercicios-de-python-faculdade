# Exercicio 19 | Plote um gráfico de linha com duas séries e adicione uma legenda para diferenciá-las

import matplotlib.pyplot as plt

# Dados
x = [1, 2, 3, 4, 5]

y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]

# Criando as duas linhas
plt.plot(x, y1, label='Série 1')
plt.plot(x, y2, label='Série 2')

# Título e rótulos
plt.title('Gráfico com Duas Séries')
plt.xlabel('X')
plt.ylabel('Y')

# Adicionando a legenda
plt.legend()

plt.show()