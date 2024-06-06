while True:
    try:
        c = float(input('Digite um valor de centimetro: '))
        # formula de conversão
        p = c / 2.54 
    except ValueError:
        print('Apenas valores númericos serão aceitos...')
    else:
        print(f'Valor lido: {c}')
        print(f'Valor convertido para polegada: {p:.2f}')
        break
