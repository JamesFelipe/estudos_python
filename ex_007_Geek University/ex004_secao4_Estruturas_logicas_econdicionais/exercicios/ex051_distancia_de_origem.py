"""
Escreva um programa que leia as coordenadas x e y de pontos no R² e calcule sua
distância da origem (0,0).
"""
from math import sqrt
x = float(input('Digite a coordenada de X: '))
y = float(input('Digite a coordeana de Y: '))
formula = sqrt(pow(y - x, 2) + pow(y - x, 2))
print(f'A distância é de {formula:.2f}')
