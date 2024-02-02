"""
Escreva um programa que receba 2 valores do tipo inteiro x e y, e calcule o valor de z:
z = (x²+ y²) / (x-y)²
"""
x = int(input('Digite o valor de x: '))
y = int(input('Digite o valor de y: '))
formula = (pow(x, 2) + pow(y, 2)) / (pow(x-y, 2))
print(f'Resultado: {formula}')
