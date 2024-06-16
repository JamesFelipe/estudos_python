"""
Faça um programa que leia um vetor de 8 posições
e, em seguida, leia também dois valores X e Y quaisquer correspondentes a duas posições no vetor. 

Ao final seu programa
deverá escrever a soma dos valores encontrados nas respectivas posições X e Y.
"""
numeros = []
for x in range(1, 9):
    numero = int(input(f'Digite o {x}º valor: '))
    numeros.append(numero)

x = int(input('Digite o valor de X[número entre 1 e 8]: '))
y = int(input('Digite o valor de y[Número entre 1 e 8]: '))
print(f'A soma dos valores na posição de x e y é: {numeros[x] + numeros[y]}')
