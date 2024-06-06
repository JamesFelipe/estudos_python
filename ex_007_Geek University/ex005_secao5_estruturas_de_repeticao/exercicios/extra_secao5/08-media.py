while True:
    try:
        print('Digite duas notas: ')
        n1 = float(input('Nota1: '))
    except ValueError:
        print('Apenas valores númericos são aceitos...')
    else:
        if n1 > 10 or n1 < 0:
            print('Nota inválido... Programa encerrado...')
        else:
            try:
                n2 = float(input('Nota2: '))
            except ValueError:
                print('Apenas valores númericos são aceitos...')
            else:
                if n2 > 10 or n2 < 0:
                    print('Nota inválida... Programa encerrado...')
                else:
                    media = (n1 + n2) / 2
                    print(f'Sua média é: {media}')
            break
