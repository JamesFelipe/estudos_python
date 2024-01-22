# Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

# Código Bard modificado
ano = int(input('Digite um ano qualquer> '))
if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print(f'O {ano} é BISSEXTO')
else:
    print(f'O {ano} não é BISSEXTO')
