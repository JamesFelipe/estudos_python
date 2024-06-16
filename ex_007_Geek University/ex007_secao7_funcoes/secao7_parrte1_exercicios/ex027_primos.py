"""
Leia 10 números inteiros e armazene em um vetor. Em seguida escreva os elementos
que são primos e suas respectivas posições no vetor.
"""
# Código ChatGpt
def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Leitura de 10 números inteiros
vetor = []
for _ in range(10):
    numero = int(input("Digite um número inteiro: "))
    vetor.append(numero)

# Encontrar e imprimir elementos primos e suas posições
print("Elementos primos e suas posições:")
for i, num in enumerate(vetor):
    if eh_primo(num):
        print(f"Posição {i}: {num}")
