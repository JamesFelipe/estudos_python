numero = 1
while numero <= 9:
    for i in range(1, 10):
        print(f'{i:<2} X {numero} = {numero * i:<2}', end=' | ')
    print()
    numero += 1
