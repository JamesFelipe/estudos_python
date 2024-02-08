# Desenvolva um programa que apresente o maior e o menor valores da sequência ([54, 10, 29, 87, 7, 64])
from functools import reduce
numeros = [54, 10, 29, 87, 7, 64]
print(f'O maior elemento da sequência é: {reduce(lambda a, b: a if a > b else b, numeros)}')
print(f'O maior elemento da sequência é: {reduce(lambda a, b: a if a < b else b, numeros)}')
