from datetime import date, datetime
atual = date.today().year
dia = int(input('Digite um dia: '))
mes = input('Digite o mês (por extenso): ').strip().title()

lista_dias = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

lista_mes = ['Janeiro', 'Fervereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 
'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

if dia in lista_dias:
    print(f'Dia {dia}', end=' ')
    if mes in lista_mes:
        print(f'de {mes} de {atual}')        
    else:
        print('Mês Inexistente')
else:
    print('Dia inexistente')
