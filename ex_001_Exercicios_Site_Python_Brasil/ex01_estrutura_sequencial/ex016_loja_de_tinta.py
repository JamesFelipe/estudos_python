"""
Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta 
a serem compradas e o preço total.
"""
area = float(input('Digite o tamanho da área a ser pintada em metros:m ')) * 3
tinta = area / 18
preco = tinta * 80
print(f'Você precisará de {tinta:.2f} latas de tinta - Preço: {preco:.2f}R$')
