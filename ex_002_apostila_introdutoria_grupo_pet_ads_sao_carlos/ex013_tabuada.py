#  Escreva um programa que leia um número de 1 a 10, e mostre a tabuada desse número.
numero = int(input('Digite um valor entre 1 e 10: '))
for i in range(1, 11):
    print(f'{i:2} X {numero} = {i * numero}')
