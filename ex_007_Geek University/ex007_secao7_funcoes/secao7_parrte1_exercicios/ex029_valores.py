"""
Faça um programa que receba 6 números inteiros e mostre:
    Os números pares digitados;
    A soma dos números pares digitados;
    Os números impares digitados;
    A quantidade de números ímpares digitados;
"""
numeros = []
for i in range(1, 7):
    numero = int(input(f'Digite o {i}º valor: '))
    numeros.append(numero)

pares = [x for x in numeros if x % 2 == 0]
impares = [x for x in numeros if x % 2 == 1]
print(f'Os números pares são: {pares}')
print(f'A soma dos números pares é: {sum(pares)}')
print(f'Os números ímpares digitados foram: {impares}')
print(f'Foram digitados {len(impares)} números ímpares')
