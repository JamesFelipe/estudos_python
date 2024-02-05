# Faça um programa que pergunte o preço de três produtos e
# # informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato
produto1 = float(input('Digite o valor do primeiro produto:R$ '))
produto2 = float(input('Digite o valor do segundo produto:R$ '))
produto3 = float(input('Digite o valor do terceiro produto:R$ '))
if produto1 < produto2 < produto3:
    print('Compre o 1º produto')
elif produto2 < produto1 < produto3:
    print('Compre o 2º produto')
elif produto3 < produto2 < produto1:
    print('Compre o 3º produto')
else:
    print('Tanto faz, os valores são iguais')
