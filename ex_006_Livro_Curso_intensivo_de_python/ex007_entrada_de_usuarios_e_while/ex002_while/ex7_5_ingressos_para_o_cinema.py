while True:
    idade = int(input('Digite sua idade[0 para encerrar]: '))
    if idade <= 3:
        print('Entrada gratuia')
    elif idade > 3 and idade <= 12:
        print('Entrada 10 Doláres')
    elif idade > 12:
        print('Entrada 15 Doláres')
    if idade == 0:
        break
