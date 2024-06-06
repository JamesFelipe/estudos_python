while True:
    try:
        n = int(input('Digite um valor entre 1 e 7: '))
    except ValueError:
        print('Apenas números inteiros são aceitos...')
    else:
        if n == 1:
            print('Domingo')
        elif n == 2:
            print('Segunda')
        elif n == 3:
            print('Terça')
        elif n == 4:
            print('Quarta')
        elif n == 5:
            print('Quinta')
        elif n == 6:
            print('Sexta')
        elif n == 7:
            print('Sábado')
        else:
            print('Número inválido')
        break
