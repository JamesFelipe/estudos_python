soma = 0
n = int(input("Digite um número inteiro positivo: "))
if n > 0:
    for i in range(0, n+1):
        soma += i
else:
    soma = 0
    print("Só aceito números inteiros positivos")
print(f"A soma dos valores é: {soma}")
