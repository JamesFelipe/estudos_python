# Leia um vetor de 10 posições. Contar e escrever quantos valores pares ele possui.
numeros = []
cont = 0
for i in range(1, 11):
    numero = int(input(f'Digite o {i}º valor: '))
    numeros.append(numero)
    
for par in numeros:
    if par % 2 == 0:
        cont += 1

print(f'Foram digitados {cont} valores pares')
