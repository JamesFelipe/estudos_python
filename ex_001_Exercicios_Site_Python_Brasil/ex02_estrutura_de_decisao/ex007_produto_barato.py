# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
# sabendo que a decisão é sempre pelo mais barato.
produto1 = float(input('Digite o preço do primeiro produto: '))
produto2 = float(input('Digite o preço do segundo produto: '))
produto3 = float(input('Digite o preço do terceiro produto: '))
if produto1 < produto2 and produto3:
    print(f'O produto mais barato custa: {produto1:.2f} R$')
elif produto2 < produto1 and produto3:
    print(f'O produto mais barato custa: {produto2:.2f} R$')
elif produto3 < produto1 and produto2:
    print(f'O produto mais barato custa: {produto3:.2f} R$')
else:
    print('Os produtos tem o mesmo precço')
