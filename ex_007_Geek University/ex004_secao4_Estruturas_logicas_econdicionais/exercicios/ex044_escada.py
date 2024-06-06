"""
Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar
subindo a escada. Calcule e mostre quantos degraus o usuário deverá subir para atingir
seu objetivo.
"""
inicio_degrau = int(input('Digite em que degrau você está: '))
fim_degrau = int(input('Digite em que degrau você quer chegar: '))
print(f'Você deverá subir {fim_degrau - inicio_degrau} degraus para atingir sue objetivo')
