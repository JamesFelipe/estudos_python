while True:
    try:
        c = float(input('Digite um temperatura em celsius: '))
        #formula de conversão
        k = c + 273.15 
    except ValueError:
        print('Digite apenas valores númericos...')
    else:
        print(f'Temperatura em celsius: {c}')
        print(f'Mesma temperatura em Kelvin: {k}')
        break
