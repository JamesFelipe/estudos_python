while True:
    try:
        print('Digite três valores')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        n3 = int(input('Digite o terceiro valor: '))
    except ValueError:
        print('Apenas valores inteiros são aceitos, Digite os valores novamente...')
    else:
        print(f'A soma entre os valores digitados é {n1 + n2 + n3}')
        break
