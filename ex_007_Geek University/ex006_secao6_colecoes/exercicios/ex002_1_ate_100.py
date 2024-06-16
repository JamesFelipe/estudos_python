"""
Escreva um programa que escreva na tela, de 1 até 100, de 1 em 1, 3 vezes. 
A primeira vez deve usar a estrutura de repetição for, 
a segunda while, e a terceira do while
"""
for i in range(1, 101, 1):
    print(i, end=" ")
print("\n")

n = 1
while n <= 100:
    print(n, end=" ")
    n += 1

# Não existe do while no python(dia 06/06/2024)
