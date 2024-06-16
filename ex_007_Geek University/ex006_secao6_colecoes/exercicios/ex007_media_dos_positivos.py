# Faça um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima sua média.
numeros, media, soma, cont = 0, 0, 0, 0

for i in range(1, 11):
    numeros = int(input(f"Digite o {i}º valor: "))
    if numeros > 0:
        cont += 1
        soma += numeros
        media = soma / cont
        
print(f"A média dos valores digitados é: {media:.2f}")
