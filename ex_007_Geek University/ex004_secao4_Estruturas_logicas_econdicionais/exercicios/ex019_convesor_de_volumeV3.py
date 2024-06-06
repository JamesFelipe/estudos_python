"""
Leia um valor de volume em litros e apresento-o convertido em metros cúbicos m³.
fórmula de conversão é: M = L / 1000, Sendo L o volume em litros e M o volume em metros cúbicos.
"""
litros = float(input('Digite um valor em litros: '))
print(F'{litros} litros em metros cúbicos é: {litros / 1000}')
