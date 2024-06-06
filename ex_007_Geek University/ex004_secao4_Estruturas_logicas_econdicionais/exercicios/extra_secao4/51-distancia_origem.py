#Formulas
# d² = x² + y²
# d = sqrt(x² + y²)

# importação da biblioteca
from math import sqrt

# entrada dos valores
x = float(input('Digite o valor de x: '))
y = float(input('Digite o valor de x: '))

# formula para que máquina entenda lol
distancia = sqrt((x - y) ** 2) 
print(f'A distância de origem é: {distancia}')
