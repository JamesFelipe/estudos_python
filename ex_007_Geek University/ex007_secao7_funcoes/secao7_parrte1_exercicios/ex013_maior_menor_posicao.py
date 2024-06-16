"""
Fazer um programa para ler 5 valores e, em seguida, mostrar a posição onde se encon-
tram o maior e o menor valor.
"""
numeros = []
for x in range(1, 6):
    numero = int(input(f'Digite o {x}º valor: '))
    numeros.append(numero)

print(f'O maior valor digitado está na posição: {numeros.index(max(numeros)) + 1}')
print(f'O menor valor digitado está na posição: {numeros.index(min(numeros)) + 1}')
