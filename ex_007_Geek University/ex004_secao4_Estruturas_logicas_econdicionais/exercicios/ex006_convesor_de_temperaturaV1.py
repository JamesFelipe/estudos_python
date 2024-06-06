"""
Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
Afórmula de conversão é: F = c * (9.0/5.0)+32.0, sendo F atemperatura em Fahrenheit
e C a temperatura em Celsius.
"""
celsius = float(input('Digite a temperatura em ºC: '))
f = celsius * (9.0/5.0) + 32
print(f'{celsius}ºC em Fahrenheit é: {f}ºF')
