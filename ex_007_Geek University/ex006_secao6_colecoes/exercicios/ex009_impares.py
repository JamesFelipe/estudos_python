# Faça um programa que leia um número inteiro N e depois imprima os N primeiros números naturais ímpares.
n = int(input("Digite um valor inteiro: "))
print(f"Ímpares naturais até {n}: ")
for i in range(1, n):
    if i % 2 == 1:
        print(i, end=" -> ")
print("Fim")
