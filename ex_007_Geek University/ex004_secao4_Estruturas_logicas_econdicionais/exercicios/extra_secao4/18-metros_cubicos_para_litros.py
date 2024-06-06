while True:
    try:
        m = float(input('Digite a quantidade de metros cubicos(m³): '))
        l = 1000 * m
    except ValueError:
        print('Apenas valores númericos serão aceitos...')
    else:
        print(f'Valor lido: {m}')
        print(f'Valor convertido para litros: {l}')
        break
