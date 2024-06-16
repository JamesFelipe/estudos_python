"""
Leia um vetor de 10 posições e atribua valor O para todos os elementos que possuírem
valores negativos.
"""
numeros = []
for i in range(1, 11):
    numero = int(input('Digite um valor inteiro: '))
    if numero < 0:
        numeros.append(0)
    else:
        numeros.append(numero)
print(f'Os números digitados foram: {numeros}')
w