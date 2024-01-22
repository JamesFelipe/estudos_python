"""
Faça um Programa que leia 2 números 
e em seguida pergunte ao usuário qual operação ele deseja realizar. 

O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.
"""
numero1  = input('Digite o primeiro valor: ')
numero2 = input('Digite o segundo valor: ')
soma = float(numero1) + float(numero2)
menu = int(input('''
==== MENU DE OPÇÕES

1 - Par ou ímpar
2 - Positivo ou negativo
3 - Inteiro ou decimal
    
    
Digite aqui sua opção escolhida(número): '''))
match menu:
    case 1:
        if soma  % 2 == 0:
            print(f'O número {soma} é Par')
        else:
            print(f'O número {soma} é Ímpar')
    case 2:
        if soma == 0:
            print('O zero é um valor nulo')
        elif soma > 0:
            print(f'O número {soma} é positivo')
        else:
            print(f'O número {soma} é negativo')
    case 3:
        # Obs.: o valor sempre vai ser decimal por causa do tipo da soma
        if '.' in numero1 or numero2:
            print(f'O número {numero1 or numero2} é um decimal')
        else:
            print(f'O número {numero1 or numero2} é inteiro')
    case _:
        print('Valor inválido')
