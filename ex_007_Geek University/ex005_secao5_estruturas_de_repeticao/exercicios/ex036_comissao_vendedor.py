"""
Escreva um programa que, dado o valor da venda, imprima a comissão que deverá ser
paga ao vendedor. Para calcular a comissão, considere a tabela abaixo:

_____________________________________________________________________________________________
|           Venda Mensal                                     |           Comissão           |
|   Maior ou igual a R$100.000,00      1                    |  R$700,00 + 16% das vendas   |
|   Menor que R$100.000,00 e maior ou igual a R$80.000,00    2|  R$650,00 +14% das vendas    |
|   Menor que R$80.000,00 e maior ou igual a R$60.000,00     3|  R$600,00 +14% das vendas    |
|   Menor que R$60.000,00 e maior ou igual a R$40.000,00     4|  R$550,00 +14% das vendas    |
|   Menor que R$40.000,00 e maior ou igual a R$20.000,00    5 |  R$500,00 +14% das vendas    |
|   Menor que R$20.000,00                                    |  R$400,00 +14% das vendas    |
---------------------------------------------------------------------------------------------
"""
venda = float(input('Digite o valor da venda: '))
if venda >= 100_000:
    comisao = venda * 0.16 + 700
    print(f'Você irá ganhar de comissão: {comisao:.2f}')
elif venda < 100_000 and venda >= 80_000:
    comisao = venda * 0.14 + 650
    print(f'Você irá ganhar de comissão: {comisao:.2f}')
elif venda < 80_000 and venda >= 60_000:
    comisao = venda * 0.14 + 600
    print(f'Você irá ganhar de comissão: {comisao:.2f}')
elif venda < 60_000 and venda >= 40_000:
    comisao = venda * 0.14 + 550
    print(f'Você irá ganhar de comissão: {comisao:.2f}')
elif venda < 40_000 and venda >= 20_000:
    comisao = venda * 0.14 + 500
    print(f'Você irá ganhar de comissão: {comisao:.2f}')
elif venda < 20_000:
    comisao = venda * 0.14 + 400
    print(f'Você irá ganhar de comissão: {comisao:.2f}')
