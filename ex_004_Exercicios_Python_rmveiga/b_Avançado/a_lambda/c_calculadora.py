"""
Desenvolva uma calculadora rudimentar onde o usuário deve informar: 
qual operação ele deseja realizar, 
quais os valores para a realização do cálculo (apenas dois valores) 
e o resultado da operação
"""
opcoes = int(input("""
            Menu de Opções
[ 1 ] Soma
[ 2 ] Subtração
[ 3 ] Multiplicação
[ 4 ] Divisão
                   
Digite aqui sua opão[Número]: """))
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
if opcoes == 1:
    soma = lambda a, b: a + b
    print(f'{a} + {b} = {soma(a, b)}')
elif opcoes == 2:
    subtracao = lambda a, b: a - b
    print(f'{a} - {b} = {subtracao(a, b)}')
elif opcoes == 3:
    multi = lambda a, b: a - b
    print(f'{a} X {b} = {multi(a, b)}')
elif opcoes == 4:
    divisao = lambda a, b: a - b
    print(f'{a} / {b} = {divisao(a, b)}')
else:
    print('Opção Inválida')
