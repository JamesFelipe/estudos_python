# Escreva um programa para encontrar a soma S = 3 + 6 + 9 + …. + 333.
soma = 0
for i in range(1, 333, 2):
    soma += i
print(f'Soma: {soma}')
