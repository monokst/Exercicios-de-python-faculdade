# Exercicio 15 | Transformada de Fourier inversa de um sinal complexo aleatório
import numpy as np
from scipy.fft import ifft

#cria um sinal complexo aleatório
sinal = np.random.random(10) + 1j * np.random.random(10)

#calcula a Transformada Inversa de Fourier
resultado = ifft(sinal)

print(resultado)