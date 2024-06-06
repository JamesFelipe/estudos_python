"""
Ler um número inteiro. Se o número lido for negativo, escreva a mensagem “Número
inválido”. Se o número for positivo, calcular o logaritmo deste numero.
"""
from math import log
numero = int(input('Digite um valor inteiro: '))
if numero > 0:
    print(f'O logaritmo de {numero} é {log(numero)}')
else:
    print('Valor inválido')
