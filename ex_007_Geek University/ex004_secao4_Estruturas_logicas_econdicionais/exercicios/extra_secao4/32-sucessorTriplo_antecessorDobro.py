while True:
    try:
        n = int(input('Digite um valor: '))
        # sucessor do triplo do valor digitado
        sucessor_triplo = n * 3 + 1 
        # antecessor do dobro do valor digitado
        antecessor_do_dobro = n * 2 - 1 
    except ValueError:
        print('Apenas valores inteiros serão aceitos...')
    else:
        print(f'Número lido: {n}')
        # abaixo a soma do sucessor do número digitado + o antecessor do valor ditiado
        print(f'Soma do sucessor do triplo do número + o antecessor de seu número: {sucessor_triplo + antecessor_do_dobro}')
        break
