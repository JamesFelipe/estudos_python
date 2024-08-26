"""
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro

Escreva um algoritmo que leia o número de litros vendidos,
o tipo de combustível (codificado da seguinte forma:
A-álcool, G-gasolina), 
calcule e imprima o valor a ser pago pelo cliente sabendo-se que
o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
"""
litros = float(input('Digite quantos litros foram vendidos: '))
tipo = input('Tipo de Combustível[A-álcool, G-gasolina]: ').strip().upper()
if tipo == 'A':
    if litros <= 20:
        total_litros = litros * 1.90
        desconto = total_litros - (total_litros * 3/100)
        print(f'Preço a ser pago no Álcool: {desconto:.2f}R$')
    elif litros > 20:
        total_litros = litros * 1.90
        desconto = total_litros - (total_litros * 5/100)
        print(f'Preço a ser pago no Álcool: {desconto:.2f}R$')
elif tipo == 'G':
    if litros <= 20:
        total_litros = litros * 2.50
        desconto = total_litros - (total_litros * 4/100)
        print(f'Preço a ser pago na Gasolina: {desconto:.2f}R$')
    elif litros > 20:
        total_litros = litros * 2.50
        desconto = total_litros - (total_litros * 6/100)
        print(f'Preço a ser pago na Gasolina: {desconto:.2f}R$')
else:
    print('Opção Inválida')
