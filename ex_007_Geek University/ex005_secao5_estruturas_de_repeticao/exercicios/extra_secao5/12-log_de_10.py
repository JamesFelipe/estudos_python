from math import log10
while True:
    try:
        n = int(input('Digite um valor: '))
    except ValueError:
        print('Apenas valores inteiros serão aceitos...')
    else:
        if n < 0:
            print('Número inválido...')
        elif n > 0:
            print(f'O logaritmo de base10 de {n} é {log10(n)}')
        break
