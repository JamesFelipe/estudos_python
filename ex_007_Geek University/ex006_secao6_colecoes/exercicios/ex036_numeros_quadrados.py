"""
Faça um programa que calcule a diferença 
entre a soma dos quadrados dos primeiros 100 números naturais
e o quadrado da soma. 

Ex: A soma dos quadrados dos dez primeiros números naturais é, 
1² + 2² +...+ 10² = 385

O quadrado da soma dos dez primeiros números naturais é,
(1+2+...+10)2= 552 = 3025

A diferença entre a soma 
dos quadrados dos dez primeiros números naturais 
e o quadrado da soma é 3025-385 2640.
"""
# quadrado da soma dos dez primeiros numeros naturais
soma1 = 0
for i in range(1, 11):
    soma1 += i
soma1 = soma1 ** 2
print(soma1)

# A soma dos quadrados dos dez primeiros números naturais
soma2 = 0
for i in range(1, 11):
    soma2 += pow(i, 2)
print(soma2)
print(soma2)

# Diferença
print(f'{soma1} - {soma2} = {soma1 - soma2}')
