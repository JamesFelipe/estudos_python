"""
Crie uma função que receba como parâmetro uma lista, com valores de qualquer tipo. A função
deve imprimir todos os elementos da lista numerando-os.
"""
def imprime_lista(lista):
    for l in enumerate(lista):
        print(l)
        

print(imprime_lista([1, 2, 3]))
        