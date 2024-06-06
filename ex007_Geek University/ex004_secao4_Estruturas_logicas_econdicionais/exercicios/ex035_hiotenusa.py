"""
Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação:
hipotenusa = √a² + b², Faça um programa que receba os valores de a e b e calcule
o valor da hipotenusa através da equação. Imprima o resultado dessa operação.
"""
from math import sqrt
a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
print(f'O valor da hipotenusa é: {sqrt(((a * 2) + (a * 2))):.2f}')
