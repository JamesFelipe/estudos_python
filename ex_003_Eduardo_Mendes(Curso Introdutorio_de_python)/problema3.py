"""Faça um programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a corbetura da tinta de 1 litro para cada 3 metros é a tinta vendida em latas de 18 litros,
que custam R$ 80,00. informe ao usuário a quantidade de latas de tinta a serem compradas e o preço total"""
tamanho = float(input('Digite o tamanho da parede a ser pintada: m² '))
tinta = (tamanho * 3) / 18
preco = tinta * 80
print(f'Você irá precisar de {tinta:.2f} latas de tinta e vai pagar {preco:.2f}R$')
