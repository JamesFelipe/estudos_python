"""
Desenvolva um programa que leia o seu nome completo
e que apresente somente o seu primeiro e último nomes
"""
nome = input('Digite seu nome completo: ')
primeiro = lambda nome: nome.split()[0]
ultimo = lambda nome: nome.split()[-1]
print(f'Seu primeiro nome é: {primeiro(nome)} e seu último nome é: {ultimo(nome)}')
