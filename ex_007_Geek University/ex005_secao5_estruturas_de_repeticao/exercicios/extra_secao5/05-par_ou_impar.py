while True:
    try:
        n = int(input('Digite um valor: '))
    except ValueError:
        print('Apenas valores inteiros são aceitos...')
    else:
        if n % 2 == 0:
            print(f'O número {n} é PAR!')
        else:
            print(f'O número {n} é ÍMPAR!')
        break
