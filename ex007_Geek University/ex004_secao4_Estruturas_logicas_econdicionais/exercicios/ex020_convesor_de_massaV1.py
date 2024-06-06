"""
Leia um valor de massa em quilogramas e apresente-o convertido em libras. A fórmula
de conversão é: L = K / 0.45. sendo K a massa em quilogramas e L a massa em libras.
"""
quilogramas = float(input(f'Digite o valor da massa em Kg: '))
print(f'{quilogramas} Kg em libras é: {quilogramas / 0.45:.2f}')
