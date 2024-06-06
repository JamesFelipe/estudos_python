while True:
    print('Digite números maiores que zero: ')
    b_menor = float(input('Digite a base menor: '))
    if b_menor <= 0:
        print('Valor inválido')
        break
    b_maior = float(input('Digite a base maior: '))
    if b_maior <= 0:
        print('Valor inválido')
        break
    al = float(input('Digite a altura: '))
    area = ((b_maior + b_menor) * al) / 2
    print(f'O trápezio tem área: {area}')
    break
