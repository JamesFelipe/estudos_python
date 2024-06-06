while True:
    try:
        raio = float(input('Digite o valor do raio do círculo: '))
        # formula para calcular a área de círculo
        c = 3.14 * (raio * raio) 
    except ValueError:
        print('Apenas valores númericos serão aceitos')
    else:
        print(f'{raio} corresponde a área do círculo: {c}')
        break
