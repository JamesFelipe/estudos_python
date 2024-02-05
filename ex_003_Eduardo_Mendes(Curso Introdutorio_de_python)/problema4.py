# Faça um programa que peça 2 números inteiros e um número float. Caclucle e mostre
# o produto do dobro do primeiro com metadade do segundo
# a soma do triplo do primeiro com o terceiro
# o terceiro elevado ao cubo
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite o mesmo/outro valor: '))
n3 = float(input('Digite o mesmo/outro valor: '))
dobro_metadade = (n1 * 2) / (n1 / 2)
triplo_mais_terceiro = (n1 * 3) + n3
print(f'o produto do dobro do primeiro com metadade do segundo é {dobro_metadade}')
print(f'a soma do triplo do primeiro com o terceiro é {triplo_mais_terceiro}')
print(f'o terceiro elevado ao cubo é: {n3 ** 3}')

