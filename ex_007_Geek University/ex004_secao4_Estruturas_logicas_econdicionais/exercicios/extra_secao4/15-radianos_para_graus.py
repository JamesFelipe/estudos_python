while True:
    try:
        radianos = float(input('Digite o ângulo radiano: '))
        PI = 3.14
        # formula de conversão
        g = radianos * 180 / PI 
    except ValueError:
        print('Apenas valores númericos serão aveitos...')
    else:
        print(f'Valor lido: {radianos}')
        print(f'Valor convertido para graus: {g:.2f}°')
        break
