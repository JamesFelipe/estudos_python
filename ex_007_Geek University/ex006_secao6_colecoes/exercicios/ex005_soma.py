# Faça um programa que peça ao usuário para digitar 10 valores e some-os.
numeros, soma = 0, 0

for i in range(1, 11):
    numeros = int(input(f"Digite o {i}º valor: "))
    soma += numeros
print(f"A soma dos valores digitados é: {soma}")
