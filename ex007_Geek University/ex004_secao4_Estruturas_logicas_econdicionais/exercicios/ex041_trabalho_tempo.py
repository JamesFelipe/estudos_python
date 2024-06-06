"""
Faça um programa que leia o valor da hora de trabalho (em reais) e número de horas
trabalhadas no mês. Imprima o valor a ser pago ao funcionário, adicionando 10% sobre
o valor calculado.
"""
hora_trabalhada_valor = float(input('Digite quanto você ganha por hora: '))
horas_trabalhadas_mes = float(input('Digite quantas horas você trabalhou no mês: '))
total = hora_trabalhada_valor * horas_trabalhadas_mes
print(f'No total você ganha: {total:.2f} R$')
print(f'Mas adicionando 10% você ganha: {total + (total * 10/100):.2f} R$')
