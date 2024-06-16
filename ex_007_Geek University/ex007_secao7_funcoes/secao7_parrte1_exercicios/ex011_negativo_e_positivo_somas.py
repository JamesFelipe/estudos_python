"""
Faça um programa que preencha um vetor com 10 números reais, calcule e mostre a
quantidade de números negativos e a soma dos números positivos desse vetor.
"""
numeros =  []
negativos = []
positivos = []
for x in range(1, 11):
    numero = float(input(f'Digite o {x}º valor: '))
    numeros.append(numero)

for num in numeros:
    if num < 0:
        negativos.append(num)
    elif num > 0:
        positivos.append(num)
print(f'Foram digitados {len(negativos)} números negativos')
print(f'A soma dos valores positivos é: {sum(positivos)}')
