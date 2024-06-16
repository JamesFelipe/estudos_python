"""
Faça um programa que leia dois vetores de 10 posições e calcule outro vetor contendo,
nas posições pares os valores do primeiro e nas posições impares os valores do se-
gundo.
"""
numeros1 = []
numeros2 = []
caluclo = []
for i in range(1, 11):
    numero = int(input('Digite um valor inteiro: '))
    numeros1.append(numero)
    
for j in range(1, 11):
    numero = int(input('Digite um valor inteiro: '))
    numeros2.append(numero)

for i in numeros1:
    if i % 2 == 0:
        caluclo.append(i)
    elif i % 2 == 1:
        caluclo.append(i)

print(caluclo)
