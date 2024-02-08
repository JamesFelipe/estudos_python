# Desenvolva um programa que leia um número inteiro qualquer e que informe se este número é par ou impar
numero = int(input('Digite um valor inteiro: '))
if numero == 0:
    print('Número neutro, nem ímpar e nem par')
else:
    if numero % 2 == 0:
        print('Número Par')
    else:
        print('Número Ímpar')
