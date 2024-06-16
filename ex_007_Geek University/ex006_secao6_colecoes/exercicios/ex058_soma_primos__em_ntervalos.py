# Faça um programa que some os números primos existentes entre a e b, 
# onde a e b são números informados pelo usuário.

# Código chatGpt(Modificado)
# Solicitar os valores de a e b ao usuário
a = int(input("Informe o valor de a: "))
b = int(input("Informe o valor de b: "))

# Garantir que a seja o menor e b seja o maior
menor = min(a, b)
maior = max(a, b)

primos = 0

# Percorrer cada número no intervalo [menor, maior]
for num in range(menor, maior + 1):
    if num > 1:  # Apenas números maiores que 1 podem ser primos
        primo = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                primo = False
                break
        if primo:
            primos += num

print(f"A soma números primos entre {a} e {b}: {primos}")
