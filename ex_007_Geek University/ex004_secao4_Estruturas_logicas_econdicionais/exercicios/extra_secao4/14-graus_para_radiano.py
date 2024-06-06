while True:
    try:
        angulo_graus = float(input('Digite o grau do ângulo: '))
        Pi = 3.14
        # formula de conversão
        r = angulo_graus * Pi / 180 
    except ValueError:
        print('Apenas valores númericos serão aceitos...')
    else:
        print(f'Valor lido: {angulo_graus}')
        print(f'Convertido para radianos: {r:.2f}')
        break
