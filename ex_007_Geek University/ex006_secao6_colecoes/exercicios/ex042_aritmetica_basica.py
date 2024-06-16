"""
Faça um programa que leia um conjunto não determinado de valores,
um de cada vez, e escreva para cada um dos valores lidos, 
o quadrado, o cubo 
e a raiz quadrada. 

Finalize a entrada de dados com um valor negativo ou zero.
"""
from math import sqrt
while True:
    numeros = int(input("Digite um valor inteiro[0 para sair]: "))
    if numeros <= 0:
        break
    else:
        print(f'Quadrado de {numeros}: {numeros*2}')
        print(f'Cubo de {numeros}: {numeros*3}')
        print(f'raiz quadrada de {numeros}: {sqrt(numeros)}')
