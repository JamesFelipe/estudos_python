while True:
    try:
        l = int(input('Lado do quadrado: '))
        # formula para calcular o lado do quadrado
        a = l*l 
    except ValueError:
        print('Apenas valores inteiros serão aceitos...')
    else:
        print(f'A área do quadrado é: {a}')
        break

