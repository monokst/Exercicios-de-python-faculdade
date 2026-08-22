# Exercicio 19 | Realize a transformada de Fourier de um sinal discreto composto de cenos e cossenos

import numpy as np
from scipy.fft import fft

#cria um conjunto de 100 pontos
n = np.arange(100)

#cria um sinal formado pela soma de seno e cosseno
sinal = np.sin(2 * np.pi * n / 10) + np.cos(2 * np.pi * n / 20)

#calcula a transformada tápida de Fourier
resultado = fft(sinal)

print(resultado)