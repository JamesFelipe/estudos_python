"""
Faça um programa que some os termos de valor par da sequência de Fibonacci, 
cujos valores não ultrapassem quatro milhões.
"""
soma = 0
t1 = 0
t2 = 1

for i in range(4_000_000):
    t3 = t1 + t2
    if t3 % 2 == 0:
        soma += t3
    if t3 > 4_000_000:
        break
    t1 = t2
    t2 = t3
    
print(soma)
