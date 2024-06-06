"""
Leia um número fornecido pelo usuário. Se esse número for positivo, calculo a raiz
quadrada do número. Se o número for negativo, mostre uma mensagem dizendo que o
número é inválido.
"""
from math import sqrt
numero = int(input('Digite um número inteiro: '))
if numero > 0:
    print(f'A raiz quadrada de {numero} é {sqrt(numero)}')
elif numero < 0:
    print('Números negativos são inválidos')
