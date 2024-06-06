while True:
    try:
        m = float(input('Digite a quantidade de Metros: '))
        # formula de conversão
        j = m / 0.91 
    except ValueError:
        print('Apenas valores númericos serão aceitos...')
    else:
        print(f'Valor lido: {m}')
        print(f'Metros convertidos para jardas: {j:.2f}')
        break
