while True:
    try:
        l = float(input('Digite a quantidade de litros: '))
        # formula de conversão
        m = l / 1000 
    except ValueError:
        print('Apenas valores númericos serão aceitos...')
    else:    
        print(f'Valor lido: {l}')
        print(f'Valor convertido para metros cúbicos: {m}')
        break
