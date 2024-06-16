"""
Faça um programa que calcule o menor número divisível por cada um dos números de 1 a 20? 
Ex: 2520 é o menor número que pode ser dividido por cada um dos números de 1 a 10, sem sobrar resto.
"""
# Código ChatGpt
numbers = list(range(1, 21))
mmc = numbers[0]
for i in range(1, len(numbers)):
    a = mmc
    b = numbers[i]
    # Calcular MDC(a, b)
    while b:
        a, b = b, a % b
    mdc = a
    # Calcular MMC usando a fórmula MMC(a, b) = (a * b) // MDC(a, b)
    mmc = mmc * numbers[i] // mdc

print("O menor número divisível por cada um dos números de 1 a 20 é:", mmc)