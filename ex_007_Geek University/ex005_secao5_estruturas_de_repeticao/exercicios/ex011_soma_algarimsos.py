"""
Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela, a
soma de todos os seus algarismos. Por exemplo, ao número 251 corresponderá o valor
8(2+5+ 1). Se o número lido não for maior do que zero, o programa terminará com a
mensagem "Número inválido”.
"""
numero = int(input('Digite um número maior que zero: '))
soma = 0
if numero > 0:
    numero2 = str(numero)
    for i in range(0, len(numero2)):
        soma += int(numero2[i])
    print(f'Números digitados foram: {numero} e sua soma é: {soma}')
else:
    print('Valor inválido')
