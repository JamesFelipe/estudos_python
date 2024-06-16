"""
Faça um programa que calcule o desvio padrão de um vetor v contendo n = 10 números,
onde m é a media do vetor.
"""
import numpy as np
numeros = [list(range(1, 11))]
print(f'O desvio padrão é: {np.std(numeros):.2f}')
print(f'A média é: {np.average(numeros)}')
