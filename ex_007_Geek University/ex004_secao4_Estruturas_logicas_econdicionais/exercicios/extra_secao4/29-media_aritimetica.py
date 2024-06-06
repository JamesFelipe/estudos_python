while True:
    try:
        print('Digite 4 notas: ')
        n1 = float(input('Nota1: '))
        n2 = float(input('Nota2: '))
        n3 = float(input('Nota3: '))
        n4 = float(input('Nota4: '))
    except ValueError:
        print('Apenas valores númericos serão aceitos... Digite tudo novamente...')
    else:
        # formula da média
        media = (n1 + n2 + n3 + n4) / 4 
        print(f'A nota aritmética é igual a {media}')
        break
