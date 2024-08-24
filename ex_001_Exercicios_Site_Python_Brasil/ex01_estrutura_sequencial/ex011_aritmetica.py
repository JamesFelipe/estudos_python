"""
Faça um Programa que peça 2 números inteiros e um número real. 
Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.
"""
numero1 = int(input('Digite o primeiro número inteiro: '))
numero2 = int(input('Digite o segundo número inteiro: '))
numero3 = float(input('Digite um número com ponto: '))
print(f'o produto do dobro do primeiro com metade do segundo é:\
{(numero1* 2) + (numero2 / 2)}')

print(f'a soma do triplo do primeiro com o terceiro é: \
{(numero1 * 3) + (numero3)}')

print(f'o terceiro elevado ao cubo é: {numero3 ** 3:.2f}')
