"""
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                   Até 5 Kg              Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da
compra ultrapassar R$ 25,00, receberá ainda um desconto de 10%
sobre este total. 

Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a
quantidade (em Kg) de maças adquiridas 
e escreva o valor a ser pago pelo cliente.
"""
kg_morangos = float(input('Digite o Kg de Morangos: '))
kg_macas = float(input('Digite o Kg de Maçãs: '))

if kg_morangos <= 5:
    preco_morango = kg_morangos * 2.50
    print(f'Você irá pagar nos morangos: {preco_morango:.2f}R$')
elif kg_morangos > 5:
    preco_morango = kg_morangos * 2.20
    print(f'Você irá pagar nos morangos: {preco_morango:.2f}')

if kg_macas <= 5:
    preco_macas = kg_macas * 1.80
    print(f'Você irá pagar nas macas: {preco_macas:.2f}R$')
elif kg_macas > 5:
    preco_macas = kg_morangos * 1.50
    print(f'Você irá pagar nas macas: {preco_macas:.2f}')

kg_total_frutas = kg_macas + kg_morangos
preco_total = preco_macas + preco_morango
if kg_total_frutas >= 8 and preco_total > 25:
    desconto = preco_total - (preco_total * 10 / 100)
    print(f'Com 10% de desconto você irá pagar: {desconto:.2f} R$')
