# Crie um programa que lê 6 valores inteiros e, 
# em seguida, mostre na tela os valores lidos.
numeros = []
for i in range(1, 7):
    numero = int(input(f'Digite o {i}º número: '))
    numeros.append(numero)
print(numeros)
