# Faça um programa que leia 5 números e informe o maior número.
numeros = []
for i in range(5):
    numero = int(input(f'Digite {i+1}º valor: '))
    numeros.append(numero)
    
print(f'O maior número digitado foi o número {max(numeros)}')
