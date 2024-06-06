while True:
    try:
        km = float(input('Digite a velocidade (Km/h): '))
         # formula de conversão
        m = km / 3.6
    except ValueError:
        print('Digite apenas valores númericos...')
    else:
        print(f'Quilômetro/hora: {km} km/h')
        print(f'O mesmo em metros por segundo: {m:.2f} m/s')
        break
