"""
Faça programas para calcular as seguintes sequências:
1 + 2 + 3 + 4 + 5 + ... + n
1 - 2 + 3 - 4 + 5 + (2n-1)
1+3+5+7+...+ (2n-1)
"""
soma1 = 0
n = int(input("Digite um valor inteiro: "))
for i in range(1, n + 1):
    soma1 += i
print(f"Sequência 1: {soma1}")

# Especificamente essa parte foi feita pelo chatGpt
resultado = 0
for i in range(1, n + 1):
    if i % 2 == 0:  # número par
        resultado -= i
    else:  # número ímpar
        resultado += i
print(f'Sequência 2: {resultado}')


soma3 = 0
for i in range(1, n + 1, 2):
# onde o último valor será excluído de maneira automatica pela função range(-1)
    soma3 += i
print(f'Sequência 3: {soma3}')
