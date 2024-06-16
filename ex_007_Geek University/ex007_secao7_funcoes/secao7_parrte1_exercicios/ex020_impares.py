"""
Escreva um programa que leia números inteiros no intervalo [0,50] e os armazene em um
vetor com 10 posições. Preencha um segundo vetor apenas com os números ímpares
do primeiro vetor. Imprima os dois vetores, 2 elementos por linha.
"""
numeros = []
impares = []
for i in range(1, 11):
    numero = int(input(f'Digite o {i}º valor entre 0 e 50: '))
    if numero < 0 or numero > 50:
        print('Valor não adicionado')
        numeros.append(0)
    else:
        numeros.append(numero)
print(numeros)
for impar in numeros:
    if impar != 0:
        if impar % 2 == 1:
            impares.append(impar)

print(f'Os números impares são: {impares}')
