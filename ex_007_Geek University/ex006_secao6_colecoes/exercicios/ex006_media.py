# Faça um programa que leia 10 inteiros e imprima sua média.
numeros, media, soma = 0, 0, 0

for i in range(1, 11):
    numeros = int(input(f"Digite o {i}º valor: "))
    soma += numeros
    media = soma / 10
print(f"A média dos valores digitados é: {media:.2f}")
