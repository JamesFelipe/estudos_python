"""Faça um Programa que peça a temperatura em graus Fahrenheit, 
transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9)."""
fahrenheit = float(input('Digite a temperatura em graus Fahrenheit: ºF '))
c = 5 * ((fahrenheit - 32) / 9)
print(f'{fahrenheit}ºF em graus celsius é: {c:.1f}ºC')
