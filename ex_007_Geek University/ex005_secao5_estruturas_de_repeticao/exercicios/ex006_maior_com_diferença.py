"""
Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles,
assim como a diferença existente entre ambos.
"""
numero1 = int(input('Digite o primeiro número inteiro: '))
numero2 = int(input('Digite o segundo número inteiro: '))
if numero1 > numero2:
    print(f'O número {numero1} é maior, tendo {numero1 - numero2} de diferença')
elif numero2 > numero1:
    print(f'O número {numero2} é maior, tendo {numero2 - numero1} de diferença')
else:
    print('Os números são iguais')
