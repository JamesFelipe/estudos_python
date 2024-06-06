"""
Usando switch, escreva um programa que leia um inteiro entre 1 e 12 e imprima o mês
correspondente a este numero. Isto é, janeiro se 1, fevereiro se 2, e assim por diante.
"""
mes = int(input('Digite um número inteiro entre 1 e 12: '))
match mes:
    case 1:
        print('Janeiro')
    case 2:
        print('Fervereiro')
    case 3:
        print('Março')
    case 4:
        print('Abril')
    case 5:
        print('Maio')
    case 6:
        print('Junho')
    case 7:
        print('Julho')
    case 8:
        print('Agosto')
    case 9:
        print('Setembro')
    case 10:
        print('Outubro')
    case 11:
        print('Novembro')
    case 12:
        print('Dezembro')
    case _:
        print('Valor inválido')
