# Exercicio 5 | Faça um gráfico de pizza para representar as porcentagens de quatro setores de mercado com rótulos personalizados.

import matplotlib.pyplot as plt

# Dados
setores = ['Tecnologia', 'Alimentação', 'Saúde', 'Educação']
porcentagens = [40, 25, 20, 15]

# Criando o gráfico de pizza
plt.pie(
    porcentagens,
    labels=setores,
    autopct='%1.1f%%'
)

plt.title('Setores de Mercado')

plt.show()