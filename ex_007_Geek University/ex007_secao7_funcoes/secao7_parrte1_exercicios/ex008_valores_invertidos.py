"""
Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos
na ordem inversa.
"""
numeros = []
for james in range(1, 7):
    numero = int(input(f'Digite o {james}º valor: '))
    numeros.append(numero)
print(f'{numeros} -> Invertido -> {sorted(numeros, reverse=True)}')
