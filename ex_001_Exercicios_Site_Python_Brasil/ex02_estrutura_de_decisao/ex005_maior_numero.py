# Faça um Programa que leia três números e mostre o maior deles.
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro número: '))
if numero1 > numero2 and numero3:
    print(f'O número {numero1} é maior')
elif numero2 > numero1 and numero3:
    print(f'O número {numero2} é maior')
elif numero3 > numero1 and numero2:
    print(f'O maior número é {numero3}')
else:
    print(f'Números iguais')
