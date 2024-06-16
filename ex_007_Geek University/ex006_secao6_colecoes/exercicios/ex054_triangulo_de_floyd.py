"""
Escreva um programa que leia um número inteiro positivo n 
e em seguida imprima n linhas do chamado Triangulo de Floyd. Para n = 6, temos:
1
2   3
4   5   6
7   8   9   10
11  12  13  14  15
16  17  18  19  20 21

"""
# Código ChatGpt(modificado)
def floyd_triangle(num_rows):
    for n in range(1, num_rows + 1):
        for k in range(1, n + 1):
            num = (n * (n - 1)) // 2 + k
            print(f"{num} ", end="")
        print()

# Definindo o número de linhas desejadas
num_rows = int(input("Digite um número inteiro positivo: "))
if num_rows < 0:
    print("Digite um número positivo meu xapa")
else:
    floyd_triangle(num_rows)
