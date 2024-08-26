"""
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual
operação ele deseja realizar. O resultado da operação deve ser acompanhado 
de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.
"""
n1 = float(input('Digite um número: '))
n2 = float(input('Digite um número: '))
operacao = int(input("""
Digite qual operação você deseja realizar:

[ 1 ] - Par ou ímpar
[ 2 ] - Positivo ou negativo
[ 3 ] - Inteiro ou decimal

Digite a aqui sua opção[Número]: """))
match operacao:
    case 1:
        if n1 % 2 == 0:
            print(f'O Número {round(n1)} é Par')
        else:
            print(F'O número {round(n1)} é Ímpar')
        if n2 % 2 == 0:
            print(f'O Número {round(n2)} é par')
        else:
            print(F'O número {round(n2)} é Ímpar')
    case 2:
        if n1 > 0:
            print(f'O Número {round(n1)} é Positivo')
        else:
            print(F'O número {round(n1)} é Negativo')
        if n2 > 0:
            print(f'O Número {round(n2)} é Positivo')
        else:
            print(F'O número {round(n2)} é Negativo')
    case 3:
        if n1 == round(n1):
            print(f'{round(n1)} é inteiro')
        else:
            print(f'{n1} é decimal')
        if n2 == round(n2):
            print(f'{round(n2)} é inteiro')
        else:
            print(f'{n2} é decimal')
    case _:
        print('Opção Inválida')
