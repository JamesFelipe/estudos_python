while True:
    try:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
    except ValueError:
        print('Só são aceitos números inteiros...')
    else:
        if n1 > n2:
            print('O primeiro valor é maior que o segundo')
        elif n2 > n1:
            print(f'O segundo valor é maior que o primeiro')
        else:
            print('Números iguais...')
        break
