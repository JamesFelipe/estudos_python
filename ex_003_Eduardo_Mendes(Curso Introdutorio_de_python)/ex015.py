# Faça um programa que dada a entrada de uma lista o programa calcule a
# combinatória de dois elemêntos e nos retorne as combinações em uma nova lista,

# Exemplo de entrada: [1, 2, 3, 4)
# Exemplo de saída: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

# Código ChatGpt Modificado
# Função para calcular fatorial
def fatorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fatorial(num - 1)

# Função para calcular combinação de uma lista de valores
def combinacao_lista(valores, k):
    n = len(valores)
    return fatorial(n) // (fatorial(k) * fatorial(n - k))

# Exemplo de uso para escolher 2 elementos de uma lista de 5 valores
lista_valores = [1, 2, 3, 4]
lista_valores2 = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
k = 2

# Calcular o número de combinações
combinacoes = combinacao_lista(lista_valores, k)
combinacoes2 = combinacao_lista(lista_valores2, k)

# Imprimir o resultado
print(f"O número de combinações de {len(lista_valores)} elementos escolhendo {k} é {combinacoes}.")
print(f"O número de combinações de {len(lista_valores2)} elementos escolhendo {k} é {combinacoes2}.")