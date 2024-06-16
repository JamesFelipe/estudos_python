# Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido.
maior = 0
menor = 99999
for i in range(1, 4):
    numeros = int(input(f"Digite o {i}º valor: "))
    if numeros > maior:
        maior = numeros
    if numeros < menor:
        menor = numeros
        
print(f"O maior valor digitado foi: {maior}")
print(f"O menor valor digitado foi: {menor}")
