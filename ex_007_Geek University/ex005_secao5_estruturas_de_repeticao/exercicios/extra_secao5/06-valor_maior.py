while True:
    try:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
    except ValueError:
        print('Apenas valores inteiros serão aceitos...')
    else:
        if n1 > n2:
            print(f'O primeiro valor é maior que o segundo tendo {n1 - n2} de diferença')
        elif n2 > n1:
            print(f'O segundo valor é maior que o primeiro tendo {n2 - n1} de diferença')
        else:
            print(f'Valores iguais não tem diferença...')
        break
