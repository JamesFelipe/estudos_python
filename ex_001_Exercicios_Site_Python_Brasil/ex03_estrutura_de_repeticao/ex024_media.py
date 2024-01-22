# Faça um programa que calcule o mostre a média aritmética de N notas.
n = int(input('Digite quantas médias você quer adcionar: '))
soma = cont = 0
for i in range(1, n + 1):
    notas = float(input(f'Digite a {i}º nota: '))
    cont += 1
    soma += notas
media = soma / cont
print(f'Você adicionou {cont} notas e a média final é: {media}')
