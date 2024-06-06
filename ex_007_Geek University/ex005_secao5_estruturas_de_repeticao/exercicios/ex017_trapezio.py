"""
Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que:

    A = (basemaior + basemenor) * altura / 2

Lembre-se a base maior e a base menor devem ser números maiores que zero.
"""
base_maior = float(input('Digite a base maior do trapezio: '))
base_menor = float(input('Digite a bae menor do trapezio: '))
altura = float(input('Digite a altura do trapezio: '))
if base_maior and base_menor >= 0:
    formula = (base_menor + base_maior) * altura / 2
    print(f'A área do trapezio é: {formula}')
else:
    print('Todas as bases tem que ser maior que zero')
