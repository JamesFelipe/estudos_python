while True:
    try:
        n = int(input('Digite um valor entre 100 e 999: '))
        u = n // 1 % 10
        d = n // 10 % 10
        c = n // 100 % 10
    except NameError:
        print('Digite valores entre 100 e 999')
    except ValueError:
        print('Digite valores inteiros...')   
    else:
        print(f'Número lido: {n}')
        print('Número gerado: ', end='')
        print(f'{u}', end='')
        print(f'{d}', end='')
        print(f'{c}')
        break
