from calendar import month
year = 2021

while True:
    try:
        mes: int = int(input('Digite um valor inteiro (entre 1 e 12): '))
    except ValueError:
        print('Apenas números inteiros serão aceitos...')
    else:
        if mes == 1:
            print(month(year, mes))
        elif mes == 2:
            print(month(year, mes))
        elif mes == 3:
            print(month(year, mes))
        elif mes == 4:
            print(month(year, mes))
        elif mes == 5:
            print(month(year, mes))
        elif mes == 6:
            print(month(year, mes))
        elif mes == 7:
            print(month(year, mes))
        elif mes == 8:
            print(month(year, mes))
        elif mes == 9:
            print(month(year, mes))
        elif mes == 10:
            print(month(year, mes))
        elif mes == 11:
            print(month(year, mes))
        elif mes == 12:
            print(month(year, mes))
        else:
            print('Valor inexistente...')
        break
