# Faça um programa que leia 5 números e informe a soma e a média dos números.
numeros = []
for i in range(5):
    numero = int(input(f'Digite {i+1}º valor: '))
    numeros.append(numero)
    
print(f'A média dos números digitados é: {sum(numeros) / len(numeros)}')
