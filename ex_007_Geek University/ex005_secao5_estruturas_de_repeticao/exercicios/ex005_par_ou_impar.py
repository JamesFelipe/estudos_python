"""
Faça um programa que receba um número inteiro e veriique se este número é par ou
impar.
"""
numero = int(input('Digite um valor inteiro: '))
if numero == 0:
    print(f'O valor é Nulo')
else:
    if numero % 2 == 0:
        print(f'O valor é Par')
    else:
        print(f'O valor é Ímpar')
