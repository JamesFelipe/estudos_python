"""
Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite um número inteiro: '))
n3 = int(input('Digite um número inteiro: '))
print(f'Ordem decrescente: {sorted([n1, n2, n3], reverse=True)}')
