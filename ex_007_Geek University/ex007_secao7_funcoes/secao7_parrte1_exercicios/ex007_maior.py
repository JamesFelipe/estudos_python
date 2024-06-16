"""
Escreva um programa que leia 10 números inteiros e os armazene em um vetor. 
Imprima o vetor, o maior elemento e a posição que ele se encontra.
"""
numeros = []
for i in range(1, 11):
    numero = int(input(f'Digite o {i}º valor: '))
    numeros.append(numero)
print(f'Os números digitados foram: {numeros}')
print(f'O maior digitado foi: {max(numeros)}')
print(f'O maior valor se encontra na posição: {numeros.index(max(numeros))}')
