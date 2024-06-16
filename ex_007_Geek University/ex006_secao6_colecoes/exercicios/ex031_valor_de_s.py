"""
Faça um programa que calcule e escreva o valor de S
s = 1/1 +  3 / 2 + 5 /3 + 7/4 ... 90/ 55
"""
s = 0
soma1 = soma2 = 0
for poderoso in range(1, 100, 2):
    soma1 += poderoso
    
for james in range(1, 51):
    soma2 += james

s = soma1 / soma2
print(f'O valor total de "S" é: {s}')
