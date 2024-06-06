from math import sqrt
while True:
    try:
        n = float(input('Digite um valor: '))
    except ValueError:
        print('Apenas valores númericos são aceitos...')
    else:
        if n > 0:
            print(f'A raiz quadrada de {n} é: {sqrt(n)}')
        else:
            print(f'Número {n} ao quadrado: {pow(n, 2)}')
        break
