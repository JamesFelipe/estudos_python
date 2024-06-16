"""
Faça um programa que receba do usuário dois vetores, A e B, com 10 números inteiros
cada. Crie um novo vetor denominado C calculando C = A - B. Mostre na tela os dados
do vetor C.
"""
a = list(range(15, 25))
b = list(range(10))
c = []
for valor1 in a:
    for valor2 in b:
        c.append(valor1 - valor2)
c = c[0: 10]
print(c)
