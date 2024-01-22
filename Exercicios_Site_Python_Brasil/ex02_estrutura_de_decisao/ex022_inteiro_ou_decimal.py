# Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.
numero = input('Digite um número qualquer: ')
if '.' in numero:
    print(f'O número {numero} é um decimal')
else:
    print(f'O número {numero} é inteiro')
