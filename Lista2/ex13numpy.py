#Exercicio 13

import numpy as np

# Cria os 10 primeiros números pares
# Começa em 0, vai até 18 e pula de 2 em 2
pares = np.arange(0, 20, 2)

# Calcula a soma cumulativa dos valores
soma_cumulativa = np.cumsum(pares)

# Mostra os números pares
print("Números pares:", pares)

# Mostra a soma cumulativa
print("Soma cumulativa:", soma_cumulativa)