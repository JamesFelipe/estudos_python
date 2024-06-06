"""
Faça um programa que leia três números inteiros positivos e efetue o cálculo de uma das
seguintes médias de acordo com um valor numérico digitado pelo usuário:

(a) Geométrica: ³√x * y * z
(b) Ponderada: x + 2 * y + 3 * z / 6
(c) Harmônica: 1 / 1/x + 1/y + 1/z
(d) Aritmética: x + y + z  / 3 
"""
x = int(input('Digite o primeiro número inteiro: '))
y = int(input('Digite o segundo número inteiro: '))
z = int(input('Digite o terceiro número inteiro: '))

menu = int(input('''
=========== Menu de Opções ===========
(1) - Média Geométrica
(2) - Média Ponderada
(3) - Média Harmônica
(4) - Média Aritmética

Digite aqui sua opção[Número]: '''))

match menu:
    case 1:
        media_geometrica = (x * y * z) ** (1/3) # a última parte aqui é sobre a raiz cúbica
        print(f'A média geométrica é: {media_geometrica}')
    case 2:
        media_ponderada = (x + 2) * (y + 3) * z / 6
        print(f'A média ponderada é: {media_ponderada}')
    case 3:
        media_harmonica = 1 / (1/x) + (1/y) + (1/z)
        print(f'A média harmônica é: {media_harmonica}')
    case 4:
        media_aritmetica = (x + y + z) / 3
        print(f'A média da aritmética é: {media_aritmetica}')
    case _:
        print('Valor inválido')
