"""
Leia um valor de área em metros quadrados m² e apresente-o convertido em acres. A
fórmula de conversão é: A = M *  0,000247, sendo M a área em metros quadrados e A
a área em acres.
"""
metros_quadrados = float(input('Digite um valor em metros quadrados: '))
print(f'{metros_quadrados} m² em acres é: {metros_quadrados * 0.000247}')
