"""
Escreva um programa que leia um número inteiro positivo n e em seguida imprima n linhas do chamado Triangulo de Pascal:
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
"""
# Código chatgpt
def coeficiente_binomial(n, k):
    if k == 0 or k == n:
        return 1
    return coeficiente_binomial(n-1, k-1) + coeficiente_binomial(n-1, k)

def triangulo_de_pascal(num_linhas):
    for linha in range(num_linhas):
        for k in range(linha + 1):
            print(coeficiente_binomial(linha, k), end=" ")
        print()

# Solicita ao usuário o número de linhas desejado
n = int(input("Digite um número inteiro positivo: "))

# Imprime o Triângulo de Pascal com n linhas
triangulo_de_pascal(n)
