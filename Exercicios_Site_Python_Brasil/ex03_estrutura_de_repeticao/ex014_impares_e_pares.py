# Faça um programa que peça 10 números inteiros, 
# calcule e mostre a quantidade de números pares e a quantidade de números impares.
par = impar = 0
for i in range(1, 11):
    numero = int(input(f'Digite {i}º valor: '))
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1

print(f'Temos no total {par} números pares')
print(f'Temos no total {impar} números ímpares')
