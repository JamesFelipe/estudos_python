while True:
    try:
        f = float(input('Digite a temperatura em Fahrenheit: '))
        #formula de conversão
        c = 5.0 * (f - 32.0) / 9.0 
    except ValueError:
        print('Apenas valores númericos serão aceitos!')
    else:
        print(f'{f}ºf convertidos em celsius é igual a: {c:.2f}')
        break
