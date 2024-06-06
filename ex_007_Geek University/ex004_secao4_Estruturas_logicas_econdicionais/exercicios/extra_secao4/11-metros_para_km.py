while True:
    try:
        m = float(input('Digite uma velocidade em metros por segundo (m/s): '))
        # formula de conversão
        km = m * 3.6 
    except ValueError:
        print('Apenas valores númericos são aceitos...')
    else:
        print(f'Velocidade em m/s: {m}')
        print(f'Mesma velocidade em Km/h: {km}')
        break
