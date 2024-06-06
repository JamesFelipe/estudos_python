"""
Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor de
seu dobro.
"""
numero = int(input('Digite um número inteiro: '))
print(f'A soma do sucessor + seu triplo com o antecessor de seu dobro é: \
{(numero * 3 + 1) + (numero * 2 - 1)}')
