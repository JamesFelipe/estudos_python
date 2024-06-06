while True:
    try:
        m = float(input('Metros quadrados(m²): '))
        # formula de conversão
        a = m * 0.000247 
    except ValueError:
        print('Apenas valores númericos serão aceitos')
    else:
        print(f'Valor lido: {m}')
        print(f'Metros cúbicos convertidos para acres: {a}')
