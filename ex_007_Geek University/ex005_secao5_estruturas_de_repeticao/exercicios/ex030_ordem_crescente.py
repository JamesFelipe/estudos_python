"""
Faça um programa que receba três números e mostre-os em ordem crescente.
"""

numero1 = int(input('Digite o primeiro valor inteiro: '))
numero2 = int(input('Digite o segundo valor inteiro: '))
numero3 = int(input('Digite o terceiro valor inteiro: '))
numeros = [numero1, numero2, numero3]
print(f'Números em ordem crescente fica: {sorted(numeros)}')
