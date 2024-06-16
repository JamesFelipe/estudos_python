# escreva um programa que leia um número inteiro não negativo n
# e imprima a soma dos n primeirosnúmeros primos

# Código ChatGpt
# Entrada do usuário
n = int(input("Digite um número inteiro não negativo: "))

# Verificação inicial para garantir que o número é não negativo
if n < 0:
    print("O número deve ser não negativo.")
else:
    soma = 0
    contador = 0
    numero = 2

    while contador < n:
        # Verificar se 'numero' é primo
        eh_primo = True
        if numero > 1:
            for i in range(2, int(numero ** 0.5) + 1):
                if numero % i == 0:
                    eh_primo = False
                    break
            if eh_primo:
                soma += numero
                contador += 1
        numero += 1

    # Exibe a soma dos primeiros n números primos
    print(f"A soma dos primeiros {n} números primos é: {soma}")
