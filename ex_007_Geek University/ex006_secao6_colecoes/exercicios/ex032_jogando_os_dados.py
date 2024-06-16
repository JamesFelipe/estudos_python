"""
Faça um programa que simula o lançamento de dois dados, d1 e d2,
n vezes, e tem como saída o número de cada dado e a relação entre eles (>,<,=) 
de cada lançamento.
"""
from random import choice
import os


opcao = input("Você quer ser d1 ou d2: ")
while True:
    # Gerando de um número aleátorio entre 1 e 6 incluídos
    d1 = choice(list(range(1, 7)))
    d2 = choice(list(range(1, 7)))

    menu = int(input("""
[ 1 ] - Girar os dados
[ 2 ] - Sair do Programa
Digite aqui sua opção[Número]: """))
    match menu:
        case 1:
            if d1 == d2:
                print(f"{d1}:{d2}, Deu empante, números iguais...")
            if d1 > d2:
                print(f"{d1} maior que {d2}, d1 ganhou...")
            else:
                print(f"{d2} maior que {d1}, d2 ganhou...")
        case 2:
            print("Programa encerrado")
            break
        case _:
            os.system("cls")
            print("Opção inválida...\nEsolha outra opção")
