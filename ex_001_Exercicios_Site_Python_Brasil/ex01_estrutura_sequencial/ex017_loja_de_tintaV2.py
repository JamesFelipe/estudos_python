"""
Faça um Programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas
e os respectivos preços em 3 situações:

comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, 
isto é, considere latas cheias.
"""
area = float(input('Digite o tamanho da área a ser pintada em metros:m ')) * 6
lata = round(area / 18, 2)
galoes = round(area / 3.6, 2)
preco_lata = lata * 80
preco_galao = galoes * 25
galao_e_lata = preco_lata + preco_galao
desconto = galao_e_lata - (galao_e_lata * 10/100)
print(f'Você precisará de {lata:.2f} latas de tinta - Preço: {preco_lata:.2f}R$')
print(f'Você precisará de {galoes:.2f} galões de tinta - Preço: {preco_galao:.2f}R$')
print(f'Você precisará de {galao_e_lata:.2f} galões e latas - Preço: {desconto:.2f}R$')
