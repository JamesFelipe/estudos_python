# Faça um programa que receba dois números e mostre qual deles é o maior.
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
if numero1 > numero2:
    print(f'O número {numero1} é maior')
elif numero2 > numero1:
    print(f'O número {numero2} é maior')
else:
    print('Os números são iguais')
