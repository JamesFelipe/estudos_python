lugares = []

while True:
    lugar = input('Se pudesse viajar para qualquer lugar do mundo, para onde você iria?[Digite sair para sair]:  ')
    lugares.append(lugar)

    if lugar == 'sair':
        break

lugares.pop()   
print(f'Lugares: {lugares}')
