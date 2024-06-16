"""
Faça um programa que leia um vetor de 10 posições e verifique se existem valores iguais
e os escreva na tela.
"""
# Código Bard
def main():
    # Declara um vetor de 10 posições
    vetor = [0] * 10

    # Lê os valores do vetor
    for i in range(len(vetor)):
        vetor[i] = int(input("Digite um valor: "))

    # Verifica se existem valores iguais
    for i in range(len(vetor)):
        for j in range(i + 1, len(vetor)):
            if vetor[i] == vetor[j]:
                print("Os valores", vetor[i], "e", vetor[j], "são iguais.")

if __name__ == "__main__":
    main()
