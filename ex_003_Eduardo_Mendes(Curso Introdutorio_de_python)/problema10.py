# Faça um programa que leia 5 números e informe o maior e o menor número
numeros = []
for i in range(5):
    n = int(input(f'Digite o {i+1}º número: '))
    numeros.append(n)
print(f'O maior número é {max(numeros)} e o menor número é: {min(numeros)}')
