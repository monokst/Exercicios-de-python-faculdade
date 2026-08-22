# Exercicio 8 | Plote um gráfico de linha com intervalos de confiança (sombreamento) para a função y = sin(x)

import matplotlib.pyplot as plt
import numpy as np

# Criando 100 valores de x entre 0 e 10
x = np.linspace(0, 10, 100)

# Calculando os valores da função seno para cada valor de x
y = np.sin(x)

# Definindo os limites superior e inferior do intervalo de confiança
limite_superior = y + 0.2
limite_inferior = y - 0.2

# Criando a linha principal da função seno
plt.plot(x, y, label='sin(x)')

# Criando o sombreamento entre os limites do intervalo de confiança
plt.fill_between(
    x,
    limite_inferior,
    limite_superior,
    alpha=0.3
)

# Adicionando título e identificando os eixos do gráfico
plt.title('Função seno com intervalo de confiança')
plt.xlabel('x')
plt.ylabel('y')

# Exibindo a legenda
plt.legend()

# Exibindo o gráfico
plt.show()