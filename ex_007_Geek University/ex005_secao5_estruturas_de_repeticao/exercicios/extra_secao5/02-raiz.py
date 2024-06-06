from math import sqrt
while True:
    try:
        n = int(input('Digite um valor: '))
    except ValueError:
        print('Apenas valores inteiros serão aceitos...')
    else:
        if n > 0:
            print(f'A raiz do número é: {sqrt(n)}')
        else:
            print('Número inválido...')
        break
