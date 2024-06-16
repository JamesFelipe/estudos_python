"""
Faça um programa que leia um vetor de 10 números. Leia um número x. Conte os
múltiplos de um número inteiro x num vetor e mostre-os na tela.
"""
# Código Bards
def main():
    # Declara um vetor de 10 posições
    vetor = [0] * 10

    # Lê os valores do vetor
    for i in range(len(vetor)):
        vetor[i] = int(input("Digite um valor: "))

    # Lê o número x
    x = int(input("Digite um número x: "))

    # Declara uma variável para armazenar o número de múltiplos de x
    contador = 0

    # Itera sobre o vetor, verificando se cada valor é múltiplo de x
    for valor in vetor:
        if valor % x == 0:
            contador += 1

    # Imprime o número de múltiplos de x
    print("O número x tem", contador, "múltiplos no vetor.")

if __name__ == "__main__":
    main()
