while True:
    try:
        n = int(input('Digite um valor: '))
    except ValueError:
        print('Apenas valores inteiros serão aceitos...')
    else:
        print(f'O sucessor de {n} é {n + 1} e seu atencessor é {n - 1}')
        break
