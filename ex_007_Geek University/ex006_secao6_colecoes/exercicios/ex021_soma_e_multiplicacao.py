"""
Faça um programa que receba dois números. Calcule e mostre:
- a soma dos números pares desse intervalo de números, incluindo os números digitados;
- a multiplicação dos números impares desse intervalo, incluindo os digitados
"""
soma = 0
multiplicao = 1
numero1 = int(input("Digite um valor inteiro: "))
numero2 = int(input("Digite o mesmo/outro valor inteiro: "))
for i in range(numero1+1, numero2+1):
    if i % 2 == 0:
        soma += i
    elif i % 2 == 1:
        multiplicao *= i
print(f"A soma dos números pares no intervalo de valores é: {soma}")
print(f"A multiplicação dos números ímpares no intervalo de valores é: {multiplicao}")
