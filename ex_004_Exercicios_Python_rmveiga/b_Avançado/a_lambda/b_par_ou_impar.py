"""
Desenvolva um programa que leia um número qualquer e informe se ele é par ou ímpar
"""
numero = int(input('Digite um valor inteiro: '))
par = lambda numero: numero % 2 == 0
if par(numero):
    print('Par')
else:
    print('Ímpar')
