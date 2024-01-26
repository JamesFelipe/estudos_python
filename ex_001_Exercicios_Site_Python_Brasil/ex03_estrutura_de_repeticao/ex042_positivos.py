"""
Faça um programa que leia uma quantidade indeterminada de números positivos 
e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. 
A entrada de dados deverá terminar quando for lido um número negativo.
"""
# Còdigo Bard
def main():
    # Contadores para cada intervalo
    contador_0_25 = 0
    contador_26_50 = 0
    contador_51_75 = 0
    contador_76_100 = 0

    # Leitura dos números
    numero = int(input("Digite um número positivo (-1 para sair): "))
    while numero >= 0:
        # Incrementa o contador do intervalo apropriado
        if numero <= 25:
            contador_0_25 += 1
        elif numero <= 50:
            contador_26_50 += 1
        elif numero <= 75:
            contador_51_75 += 1
        else:
            contador_76_100 += 1

        # Lê o próximo número
        numero = int(input("Digite um número positivo (-1 para sair): "))

    # Exibe os resultados
    print("Números no intervalo [0-25]:", contador_0_25)
    print("Números no intervalo [26-50]:", contador_26_50)
    print("Números no intervalo [51-75]:", contador_51_75)
    print("Números no intervalo [76-100]:", contador_76_100)


if __name__ == "__main__":
    main()
