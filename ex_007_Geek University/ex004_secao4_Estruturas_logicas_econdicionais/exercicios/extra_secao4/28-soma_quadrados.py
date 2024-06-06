while True:
    try:
        print('Digite três valores inteiros:')
        n1 = int(input('Valor1: '))
        n2 = int(input('Valor2: '))
        n3 = int(input('Valor3: '))
        # formula do calculo
        quadrados = (n1 * 2) + (n2 * 2) + (n3 * 2) 
    except ValueError:
        print('Apenas valores inteiros serão aceitos... Digite tudo novamente...')
    else:
        print(f'A soma dos quadrados é igual a: {quadrados}')
        break
