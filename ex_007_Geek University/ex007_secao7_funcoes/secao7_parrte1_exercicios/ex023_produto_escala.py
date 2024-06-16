"""
Ler dois conjuntos de números reais, armazenando-os em vetores e calcular o produto
escalar entre eles.

Os conjuntos têm 5 elementos cada. Imprimir os dois conjuntos e o
produto escalar, sendo que o produto escalar é dado por x1 * y1 + x2 + y2 + ... xn * yn
"""
# Código chatGpt
# Função para calcular o produto escalar entre dois vetores
def produto_escalar(vetor1, vetor2):
    resultado = 0
    for x, y in zip(vetor1, vetor2):
        resultado += x * y
    return resultado

# Função para ler um conjunto de números reais a partir do usuário
def ler_vetor():
    vetor = []
    for i in range(5):
        elemento = float(input(f"Informe o elemento {i+1}: "))
        vetor.append(elemento)
    return vetor

# Leitura dos dois conjuntos de números reais
print("Digite os elementos do primeiro conjunto:")
conjunto1 = ler_vetor()

print("\nDigite os elementos do segundo conjunto:")
conjunto2 = ler_vetor()

# Cálculo do produto escalar
resultado_escalar = produto_escalar(conjunto1, conjunto2)

# Impressão dos conjuntos e do produto escalar
print(f"\nConjunto 1: {conjunto1}")
print(f"Conjunto 2: {conjunto2}")
print(f"Produto Escalar: {resultado_escalar}")
