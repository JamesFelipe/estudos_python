"""
Faça um Programa que peça dois números e imprima o maior deles.
"""
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
if n1 == n2:
    print('Números iguais')
elif n1 > n2:
    print(f'{n1} maior que {n2}')
elif n2 > n1:
    print(f'{n2} maior que {n1}')
