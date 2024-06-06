while True:
    try:
        m = float(input('Metros quadrados (m²): '))
        # formula de conversão
        h = m * 0.0001 
    except ValueError:
        print('Apenas valores númericos serão aceitos...')
    else:
        print(f'Valor lido: {m}')
        print(f'Metros quadrados convertidos em hectares: {h}')
        break
