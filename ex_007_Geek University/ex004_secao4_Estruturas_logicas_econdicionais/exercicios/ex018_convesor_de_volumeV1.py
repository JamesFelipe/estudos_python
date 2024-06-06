"""
Leia um valor de volume em metros cúbicos m³ e apresente-o convertido em litros. A
fórmula de conversão é: L = 1000 * M A, sendo L o volume em litros e M o volume em
metros cúbicos.
"""
metros_cubicos = float(input('Digite o valor dos metros cubicos: '))
print(f'{metros_cubicos} m³ em litros é: {1_000 * metros_cubicos}')
