"""
Faça um programa que pergunte o preço de três produtos
e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato.
"""
prod1 = float(input('Informe o preço do primeiro produto: '))
prod2 = float(input('Informe o preço do segundo produto: '))
prod3 = float(input('Informe o preço do terceiro produto: '))
print(f'O produto mais barato custa: {min([prod1, prod2, prod3])}')
