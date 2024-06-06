"""
Leia um ângulo em graus e apresente-o convertido em radianos. A fórmula de conversão
é: R = G * pi / 180, sendo G o ângulo em graus e R em radianos e pi = 3.14.
"""
from math import radians
angulo = float(input('Digite um ângulo: '))
print(f'{angulo} graus em radianos é: {angulo * 3.14 / 180:.2f}')
print(f'{angulo} graus em radianos é: {radians(angulo):.2f}')
