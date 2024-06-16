# Faça um programa que calcule a soma de 
# todos os números primos abaixo de dois milhões.

# Código ChatGpt(Modificado)
# Verificação inicial para garantir que o número é não negativo

soma = 0
contador = 0
numero = 2

while contador < 2_000_001:
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
print(f"A soma dos primeiros 2_000_001 números primos é: {soma}")
