# Calculo de Delta
a: float = float(input('Digite o valor de A: '))
b: float = float(input('Digite o valor de B: '))
c: float = float(input('Digite o valor de C: '))
delta = b ** 2 - 4 * a * c # formula para achar o delta
print(f'O valor de Delta é: {delta}')


if delta < 0:
    print('Não existe Raiz')
elif delta == 0:
    print(f'{delta}')
    print(f'Raiz única')
elif delta > 0:
    # Baskhara
    baMais = (b + pow(delta, 1/2)) / 2 * a # bhaskara positiva
    print(f'Resultado do + da formúla de Baskhara: {baMais}')

    baMenos = (b - pow(delta, 1/2)) / 2 * a # bhaskara negativa
    print(f'Resultado do - da formúla de Baskhara: {baMenos}')
