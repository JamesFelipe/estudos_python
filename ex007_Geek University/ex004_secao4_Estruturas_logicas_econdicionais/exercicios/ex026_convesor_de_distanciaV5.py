"""
Leia um valor de área em metros quadrados m² e apresente-o convertido em hectares.
A fórmula de conversão é: H = M * 0,0001, sendo M a área em metros quadrados e H
a área em hectares.
"""
metros_quadrados = float(input('Digite um valor em metros quadrados: '))
print(f'{metros_quadrados} m² em hectares é: {metros_quadrados * 0.0001}')
