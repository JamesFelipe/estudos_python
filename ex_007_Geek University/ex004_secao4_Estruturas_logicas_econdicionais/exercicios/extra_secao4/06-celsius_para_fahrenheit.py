while True:
    try:
        c = float(input('Digite um temperatura: '))
    except ValueError:
        print('Apenas valores númericos serão aceitos!')
    else:
         #formula de conversão
        f = c * (9.0 / 5.0) + 32
        print(f'{c}ºC convertidos em Fahrenheit é igual a: {f}')
        break
