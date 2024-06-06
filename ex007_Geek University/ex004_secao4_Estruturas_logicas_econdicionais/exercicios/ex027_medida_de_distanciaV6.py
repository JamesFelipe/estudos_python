"""
Leia um valor de área em hectares e apresente-o convertido em metros quadrados m?.
A fórmula de conversão é: M = H * 10_000, sendo M a área em metros quadrados e H
a área em hectares.
"""
hectares = float(input(f'Digite um valor em hectares: '))
print(f'{hectares} hecatares em metros quadrados é: {hectares * 10_000}')
