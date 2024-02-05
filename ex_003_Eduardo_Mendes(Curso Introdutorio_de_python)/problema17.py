# Faça um programa, com uma função, que calcula a mediana de uma lista
# Funções embutidas que podem te ajudar
    # sorted(lista) -> ordena a lista
lista = [1, 3, 4, 5, 7, 8]
def mediana_lista(lista):
    lista_ordenada = sorted(lista)
    if len(lista_ordenada) % 2 == 0:
        soma_par = lista_ordenada[1] + lista_ordenada[2] / len(lista_ordenada)
        return f'A mediana é: {soma_par:.2f}'
    else:
        return f'A mediana é: {lista_ordenada[2]}'

print(mediana_lista(lista))


        