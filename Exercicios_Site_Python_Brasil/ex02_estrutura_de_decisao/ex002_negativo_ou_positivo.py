# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
numero = int(input('Digite um valor inteiro: '))
if numero == 0:
    print(f'O número zero não é nem positivo nem negativo')
else:
    if numero < 0:
        print(f'O número {numero} é negativo')
    else:
        print(f'O número {numero} é positivo')
