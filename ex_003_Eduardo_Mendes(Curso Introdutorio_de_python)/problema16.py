# Faça um programa, com uma função, que calcula a média de uma lista
# Funções embutidas que podem te ajudar:
# len(lista) -> calcula o tamanho da lista
# sum(lista) -> faz a somatório dos valores
def media_lista(lista):
    return f'A média da lista é {sum(lista) / len(lista)}'

numeros = [10, 10, 10, 10]
print(media_lista(numeros))
