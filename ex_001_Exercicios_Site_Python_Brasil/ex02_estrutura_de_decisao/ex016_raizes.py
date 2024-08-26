"""
Faça um programa que calcule as raízes de uma equação do segundo grau,
na forma ax2 + bx + c. O programa deverá pedir os valores de
a, b e c e fazer as consistências,

informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, 
a equação não é do segundo grau e o programa não deve fazer pedir os
demais valores, sendo encerrado;

Se o delta calculado for negativo, a equação não possui raizes reais.
Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real;
informe-a ao usuário;

Se o delta for positivo, a equação possui duas raiz reais;
informe-as ao usuário;
"""
a = float(input('Digite o valor de A: '))
if a == 0:
    print('Equação não é de segundo grau - Programa encerrado...')
else:
    b = float(input('Digite o valor de B: '))
    c = float(input('Digite o valor de C: '))
delta = pow(b, 2) - 4 * a * c
if delta < 0:
    print('Delta Negativo - Não possui raízes reais - Programa encerrado...')
elif delta == 0:
    print(f'Delta possui apenas uma raíz real - Delta: {delta}')
elif delta > 0:
    print(f'Delta possui duas raizes reais - Delta: {delta}')
