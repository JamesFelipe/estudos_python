# Faça um Programa que peça dois números e imprima o maior deles.
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
if numero1 > numero2:
    print(f'O maior número é o {numero1}')
elif numero2 > numero1:
    print(f'O maior número é o {numero2}')
else:
    print(f'Os números são iguais')
