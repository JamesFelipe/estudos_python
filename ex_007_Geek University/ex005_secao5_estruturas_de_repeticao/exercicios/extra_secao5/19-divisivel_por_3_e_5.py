while True:
    try:
        n1: int = int(input('Digite um número: '))
    except ValueError:
        print('Apenas valores inteiros serão aceitos...')
    else:
        if n1 % 3 == 0 and n1 % 5 == 0:
            print(f'{n1} divisivel por 3 e 5')
        else:
            print(f'O número {n1} não é divisivel por 3 e 5')
        break
