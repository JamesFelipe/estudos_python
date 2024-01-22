"""
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
a - Álcool:
b - até 20 litros, desconto de 3% por litro
c - acima de 20 litros, desconto de 5% por litro
d - Gasolina:
e - até 20 litros, desconto de 4% por litro
f - acima de 20 litros, desconto de 6% por litro

Escreva um algoritmo que leia o número de litros vendidos,
o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), 
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
"""
litros = int(input('Digite quantos litros você quer comprar L: '))
opcao = int(input('''Opções Disponíveis
1 - Álcool
2- Gasolina

Digite aqui a sua opção[número]:'''))
if opcao == 1:
    if litros <= 20:
        desconto = (litros * 1.90) - (litros * 3/100)
        print(f'Com desconto de 3% você irá pagar {desconto:.2f} R$')
    elif litros > 20:
        desconto = (litros * 1.90) - (litros * 5/100)    
        print(f'Com desconto de 5% você irá pagar {desconto:.2f} R$')
elif opcao == 2:
    if litros <= 20:
        desconto = (litros * 2.50) - (litros * 4/100)
        print(f'Com desconto de 3% você irá pagar {desconto:.2f} R$')
    elif litros > 20:
        desconto = (litros * 2.50) - (litros * 6/100)
        print(f'Com desconto de 3% você irá pagar {desconto:.2f} R$')
else:
    print('Opção Inválida')
