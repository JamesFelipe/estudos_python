while True:
    try:
        j = float(input('Qauntidade de jardas: '))
        # formula de conversão
        m = 0.91 * j 
    except ValueError:
        print('Apenas valores númericos serão aceios...')
    else:
        print(f'Valor lido: {j}')
        print(f'Valor convertido para metros: {m}')
        break
