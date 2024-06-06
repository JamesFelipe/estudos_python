"""
Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro. O volume
de um cilindro circular é calculado por meio da seguinte tórmula: V = raio² * altura,
onde x = 3.14158
"""
altura = float(input('Digite a alutra do cilindo circular: '))
raio = float(input('Digite a altura do raio: '))
print(f'O volume do cilindro circular é: {pow(raio, 2) * altura}')
