while True:
    try:
        km = float(input('Digite a distância em quilômetros: '))
        # formula de conversão
        m = km / 1.61 
    except ValueError:
        print('Apenas valores númericos serão aceitos')
    else:
        print(f'Km digitados: {km}')
        print(f'Mesmo valor em milhas: {m:.2f}')
        break
