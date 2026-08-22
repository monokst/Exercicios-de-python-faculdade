# Exercicio 18 | Crie um gráfico de barras com valores positivos e negativos e use diferentes cores para cada tipo de valor

import matplotlib.pyplot as plt

# Dados
categorias = ['A', 'B', 'C', 'D', 'E']
valores = [20, -15, 30, -10, 25]

# Definindo uma cor para valores positivos e outra para negativos
cores = ['green' if valor >= 0 else 'red' for valor in valores]

# Criando o gráfico
plt.bar(categorias, valores, color=cores)

plt.title('Valores Positivos e Negativos')
plt.xlabel('Categorias')
plt.ylabel('Valores')

plt.axhline(0, color='black', linewidth=0.8)

plt.show()