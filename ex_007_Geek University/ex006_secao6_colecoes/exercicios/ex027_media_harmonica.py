"""
Em Matemática, o número harmônico designado por H(n) 
define-se como sendo a soma da série harmónica: H(n)=1+1/2+1/3+ 1/4 + ... + 1/n
Faça um programa que leia um valor inteiro e positivo e apresente o valor de H(n).
"""
# código ChatGpt
n = int(input("Digite um número inteiro e positivo: "))

if n <= 0:
    print("Por favor, digite um número inteiro e positivo.")
else:
    harmonic_number = 0
    for i in range(1, n + 1):
        harmonic_number += 1 / i
    
    print(f"O número harmônico H({n}) é: {harmonic_number:.2f}")
