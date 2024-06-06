while True:
    try:
        n = float(input('Digite um valor real: '))
    except ValueError:
        print('Apenas valores númericos são aceitos... Digite novamente...')
    else:
        print(f'O quadrado de {n} é {n*2}')
        break
