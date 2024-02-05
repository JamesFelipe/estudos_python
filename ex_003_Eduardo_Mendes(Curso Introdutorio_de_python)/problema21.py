# Dada uma lista de entradas do usuário de números inteiros, construa um dicionário com a lista padrão,
# a lista dos valores elevados ao quadrado
# e a lista dos valores elevados ao cubo
def quadrado(lista_de_numeros):
    lista_respostas = []
    for numero in lista_de_numeros:
        lista_respostas.append(numero ** 2)

    return lista_respostas

def cubo(lista_de_numeros):
    lista_respostas = []
    for numero in lista_de_numeros:
        lista_respostas.append(numero ** 3)
    return lista_respostas        
lista_valores = []
for valor in range(10):
    lista_valores.append(int(input('Fala um número aí: ')))

dicionario = {
    'lista padrão': lista_valores,
    'lista quadrada': quadrado(lista_valores),
    'lista cúbica': cubo(lista_valores)
}

for i, j in dicionario.items():
    print(f'{i}: {j}')
    