while True:
    try:
        n = float(input('Digite um valor: '))
    except ValueError:
        print('Apenas valores númericos são aceitos...')
    else:
        print(f'O número digitado foi: {n}')
        break
