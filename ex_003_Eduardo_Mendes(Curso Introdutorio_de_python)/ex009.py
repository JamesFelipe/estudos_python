""" Faça um programa que peça uma nota, entre zero e dez. 
Mostre uma mensagem caso o valor seja inválido e continue
pedindo até que o usuário informe um valor válido"""

nota = 0
while True:
    nota = int(input('Digite uma nota entre zero e dez: '))
    if nota >= 0 and nota <= 10:
        break
    else:
        print('Esse valor é inválido. Digite outro valor...')