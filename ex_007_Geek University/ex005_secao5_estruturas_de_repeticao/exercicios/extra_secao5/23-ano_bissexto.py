ano = int(input('Digite o ano: '))
if ano % 400 == 0 and ano % 4 == 0 and ano % 100 == 0:
    print(f'{ano} é BISSEXTO!')
else:
    print(f'{ano} não é bissexto!')
