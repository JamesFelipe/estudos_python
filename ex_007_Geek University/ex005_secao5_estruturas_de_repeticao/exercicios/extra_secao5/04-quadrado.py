from math import sqrt
while True:
    try:
        n = int(input('Digite um valor: '))
    except ValueError:
        print('Apenas valores inteiros são aceitos...')
    else:
        if n > 0:
            print(f'{n} ao quadrado: {n**2}')
            print(f'{sqrt(n):.2f} raiz de {n}')
        break
