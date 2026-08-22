# Exercicio 5 | Transformada de Fourier de um sinal composto por sen(2*pi*t) e cos(4*pi*t)
import numpy as np
from scipy.fft import fft

# Cria 1000 pontos entre 0 e 1
t = np.linspace(0, 1, 1000, endpoint=False)

# Cria um sinal formado pela soma de seno e cosseno
sinal = np.sin(2 * np.pi * t) + np.cos(4 * np.pi * t)

resultado = fft(sinal)

print(resultado)