while True:
    try:
        n = int(input('Digite um valor inteiro: '))
    except ValueError:
        print('Apenas valores inteiros são aceitos...')
    else:
        print(f'A quinta parte de {n} é: {n/5}')
        break
