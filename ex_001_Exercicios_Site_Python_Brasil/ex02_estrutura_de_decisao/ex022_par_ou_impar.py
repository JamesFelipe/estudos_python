"""
Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
Dica: utilize o operador módulo (resto da divisão).
"""
n = int(input('Digite um valor inteiro: '))
if n % 2 == 0:
    print(f'{n} é Par')
else:
    print(f'{n} é Ímpar')
