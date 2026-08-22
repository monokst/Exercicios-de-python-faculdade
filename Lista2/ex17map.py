# Exercicio 17 | Plote um gráfico de linha e salve-o como um arquivo PDF

import matplotlib.pyplot as plt

# Dados
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Criando o gráfico
plt.plot(x, y)

plt.title('Gráfico de Linha')
plt.xlabel('x')
plt.ylabel('y')

# Salvando como PDF
plt.savefig('grafico.pdf')

plt.show()