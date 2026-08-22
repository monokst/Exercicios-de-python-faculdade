#Exercicio 1 | Criar data frame

import pandas as pd

dados = {'Produto': ['paçoca','refrigerante','feijão','arroz','sucrilhos'],
         'Preço': ['1,00', '5,00', '8,00', '10,00', '18,00'],
         'quantidade': ['3','2', '1', '2', '1']

}

df = pd.DataFrame(dados)

print(df)