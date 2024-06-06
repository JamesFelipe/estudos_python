while True:
    try:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
    except ValueError:
        print('Apenas valores inteiros serão aceitos...')
    else:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
        elif n2 > n1:
            print(f'{n2} é maior que {n1}')
        else:
            print('Os valores são iguais')
        break
