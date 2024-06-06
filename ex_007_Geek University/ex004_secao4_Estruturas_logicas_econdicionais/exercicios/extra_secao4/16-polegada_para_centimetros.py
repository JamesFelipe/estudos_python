while True:
    try:
        p = float(input('Digite um comprimento de polegadas: '))
        # formula de conversão
        c = p * 2.54 
    except ValueError:
        print('Apenas valores númericos serão aceitos...')
    else:
        print(f'Polegada lida:> {p}')
        print(f'convertida para centímetros: {c}')
        break
