"""
Faça um programa que leia um vetor de 15 posições e o compacte,
ou seja, elimine as posições com valor zero. 
Para isso, todos os elementos à frente do valor zero, 
devem ser movidos uma posição para trás no vetor.
"""
numeros = []
for x in range(1, 16):
    numero = int(input('Digite um valor: '))
    if numero != 0:
        numeros.append(numero)

print(numeros)
