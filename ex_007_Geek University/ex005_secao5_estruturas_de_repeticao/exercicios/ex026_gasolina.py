"""
Leia a distância em Km e a quantidade de litros de gasolina consumidos por um carro
em um percurso, calcule o consumo em Km /l e escreva uma mensagem de acordo com
a tabela abaixo:

CONSUMO      | (Km/l) | MENSAGEM

menor que    | 8      | Venda o carro!
entre        | 8 e 14 | Econômico!
maior que    | 12     | Supereconômico!
"""
km = float(input('Digite a distância pecorida em Km: '))
litros = float(input('Digite quantos litros de gasolina foram gastos: '))
calculo = km / litros
print(calculo)
if calculo <= 8:
    print('Venda o Carro!')
elif calculo > 8 and calculo <= 14:
    print('Econômico!')
elif calculo >= 12.0:
    print('SuperEconômico')
