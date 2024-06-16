"""
Faça um vetor de tamanho 50 preenchido com o seguinte valor: (i + 5 * i)% (i +11), sendo
i a posição do elemento no vetor. Em seguida imprima o vetor na tela.
"""
# Código Bard
def main():
    # Declara um vetor de 50 posições
    vetor = [0] * 50

    # Itera sobre o vetor
    for i in range(len(vetor)):
        # Calcula o valor a ser armazenado no vetor
        valor = (i + 5 * i) % (i + 11)

        # Armazena o valor no vetor
        vetor[i] = valor

    # Imprime o vetor
    for valor in vetor:
        print(valor)

if __name__ == "__main__":
    main()
