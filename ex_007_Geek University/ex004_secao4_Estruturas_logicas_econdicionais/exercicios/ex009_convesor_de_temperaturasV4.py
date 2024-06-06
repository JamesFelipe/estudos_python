"""
Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin. A
fórmula de conversão é: K = c + 273.15, sendo C a temperatura em Celsius e K a
temperatura em Kelvin.
"""
celsius = float(input('Digite uma temperatura em graus celsius ºC: '))
kelvin = celsius + 273.15
print(f'{celsius}ºC em Kelvin é: {kelvin} ºK')
