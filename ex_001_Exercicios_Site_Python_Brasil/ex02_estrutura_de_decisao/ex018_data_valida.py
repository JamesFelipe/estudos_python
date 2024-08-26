"""
Faça um Programa que peça uma data no formato dd/mm/aaaa e
determine se a mesma é uma data válida.
"""
data = input('Digite uma data no formato dd//mm/aaaa: ').strip().split('/')
if (int(data[0]) > 0 and int(data[0]) <= 31) and int(data[1]) > 0 and int(data[1]) <= 12 and int(data[2]) > 0 and len(data[2]) == 4:
    print('Data Válida')
else:
    print('Data inválida')
