# Faça um programa que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
while True:
    nota = input('Digite uma nota entre 0 e 10: ')
    if nota in str(list(range(11))) :
        print(f'Nota {nota} Registrada')
        break
    else:
        print('Valor inválido...Digite uma nota válida entre 0 e 10')
