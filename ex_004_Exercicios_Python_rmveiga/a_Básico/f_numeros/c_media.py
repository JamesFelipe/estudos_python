# Desenvolva um programa que leia quatro notas e que apresente a média final
cont = soma  = 0
for i in range(1, 5):
    numero = float(input(f'Digite a nota {i}: '))
    cont += 1
    soma += numero

print(f'Sua média é: {soma / cont}')
