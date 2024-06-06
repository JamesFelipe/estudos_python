"""
Faça um programa que mostre ao usuário um menu com 4 opções de operações ma-
temáticas (as básicas, por exemplo). O usuário escolhe uma das opções e o seu pro-
grama então pede dois valores numéricos e realiza a operação, mostrando o resultado e
saindo.
"""
print('''
================ Menu de Opções ================
1 - [Adição]
2 - [Subtração]
3 - [Multiplicação]
4 - [Divisão]
''')
opcao = int(input('Digite aqui sua opção [Número]: '))
match opcao:
    case 1:
        numero1 = int(input('Digite o primeiro valor inteiro: '))
        numero2 = int(input('Digite o segundo valor inteiro: '))
        print(f'{numero1} + {numero2} = {numero1 + numero2}')
    case 2:
        numero1 = int(input('Digite o primeiro valor inteiro: '))
        numero2 = int(input('Digite o segundo valor inteiro: '))
        print(f'{numero1} - {numero2} = {numero1 - numero2}')
    case 3:
        numero1 = int(input('Digite o primeiro valor inteiro: '))
        numero2 = int(input('Digite o segundo valor inteiro: '))
        print(f'{numero1} X {numero2} = {numero1 * numero2}')
    case 4:
        numero1 = int(input('Digite o primeiro valor inteiro: '))
        numero2 = int(input('Digite o segundo valor inteiro: '))
        if numero1 == 0 or numero2 == 0:
            print('Não é possível usar zero na divisão...Programa Encerrado.')
        else:
            print(f'{numero1} / {numero2} = {numero1 / numero2}')
    case _:
        print('Valor inválido')
