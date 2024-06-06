while True:
    try:
        k = float(input('Digite a temperatura Kelvin por favor: '))
        #formula de conversão
        c = k - 273.15 
    except ValueError:
        print('Apenas valores númericos serão aceitos!')
    else:
        print(f'Temperatura em Kelvin: {k}')
        print(f'Mesma temperatura em Celsius: {c}')
        break
