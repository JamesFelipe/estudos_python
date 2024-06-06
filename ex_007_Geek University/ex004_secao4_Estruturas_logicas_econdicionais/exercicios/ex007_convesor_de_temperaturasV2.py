"""
Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
A fórmula de conversão é: C = 5.0 + (F — 32.0)/9.0, sendo C a temperatura em Celsius
e F a temperatura em Fahrenheit.
"""
fahrenheit = float(input('Digite uma temperatura em graus Fahrenheit ºF: '))
celsius = (fahrenheit - 32.0) / 9.0
print(f'{fahrenheit}ºF em celsius é: {celsius}ºC')
