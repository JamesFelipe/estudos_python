"""
Crie um programa que lê 6 valores inteiros pares e, em seguida, mostre na tela os valores
lidos na ordem inversa.
"""
numeros = []
for x in range(1, 7):
    numero = int(input(f'Digite o {x}º valor par: '))
    if numero % 2 == 0:
        numeros.append(numero)

numeros.reverse()
print(numeros)
