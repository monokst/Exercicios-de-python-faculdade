#Exercicio 9
import numpy as np

array = np.random.randint(1,101,10)

# Normaliza os valores para ficarem entre 0 e 1
array_normais = (array - np.min(array)) / ( #a divisão transforma os valores para a escala 0 até 1.
    np.max(array) - np.min(array) # calcula a diferença entre o maior e o menor.
)

print("\n - Array original:", array)
print("\n - Array normal: ", array_normais)