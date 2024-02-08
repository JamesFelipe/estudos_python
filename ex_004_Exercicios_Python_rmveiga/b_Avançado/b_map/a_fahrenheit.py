"""
Desenvolva um programa que converta todas as temperaturas 
desta lista em Celsius ([22.5, 40, 13, 29, 34]) para Fahrenheit
"""
x = map(lambda a: (a * 9/5) + 32, [22.5, 40, 13, 29, 34])
print(list(x))
