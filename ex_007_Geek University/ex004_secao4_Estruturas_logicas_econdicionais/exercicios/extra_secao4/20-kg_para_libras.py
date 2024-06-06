while True:
    try:
        kg = float(input('Quantos quilogramas meu rei/rainha: '))
        # formula de conversão
        l = kg / 0.45 
    except ValueError:
        print('Só serão aceitos valores númericos...')
    else:
        print(f'Valor lido: {kg}')
        print(f'Valor convertido para libras: {l:.2f}')
        break
