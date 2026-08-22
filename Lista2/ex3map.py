# Exercicio 3 | Gere um histograma para 500 números inteiros gerados aleatoriamente entre 0 e 100.

import matplotlib.pyplot as plt
import numpy as np

# Gerando 500 números aleatórios
dados = np.random.randint(0, 101, 500)

# Criando o histograma
plt.hist(dados, bins=10)

plt.title('Histograma')
plt.xlabel('Valores')
plt.ylabel('Frequência')

plt.show()