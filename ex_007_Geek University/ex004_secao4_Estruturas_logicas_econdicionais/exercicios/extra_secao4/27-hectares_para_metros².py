while True:
    try:
        h = float(input('Digite os hectares: '))
        # formula de conversão
        m = h * 10_000 
    except ValueError:
        print('Apenas valores númericos serão aceitos...')
    else:
        print(f'Valor lido: {h}')
        print(f'Valor convertido para metros quadrados: {m}')
        break
