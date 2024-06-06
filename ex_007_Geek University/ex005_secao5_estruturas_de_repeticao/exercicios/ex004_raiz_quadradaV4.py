"""
Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:
    O número digitado ao quadrado
    A raiz quadrada do número digitado
"""
numero = int(input('Digite um valor inteiro: '))
if numero > 0:
    print(f'{numero}² = {numero ** 2}')
    print(f'Raiz de {numero} é: {numero ** (1/2)}')
else:
    print('Só faça calculos para valores positivos')
