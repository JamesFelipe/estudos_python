"""
Faça um programa que receba do usuário um vetor com 10 posições. Em seguida deverá
ser impresso o maior e o menor elemento do vetor.
"""
numeros = []
for x in range(1, 11):
    numero = int(input(f'Digite o {x}º valor: '))
    numeros.append(numero)

print(f'O menor valor digitado foi: {min(numeros)}')
print(f'O maior valor digitado foi: {max(numeros)}')
