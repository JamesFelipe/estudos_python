"""
Escreva um programa que leia um número inteiro
e calcule a soma de todos os divisores desse número, com exceção dele próprio.
Ex: a soma dos divisores do número 66 é 1+2+3+6+11 +22 + 33 = 78
"""

numero = int(input("Digite um valor inteiro: "))
soma = 0
for i in range(1, numero):
    if numero % i == 0:
        soma += i
print(f'A soma dos divisores de {numero} é: {soma}')
