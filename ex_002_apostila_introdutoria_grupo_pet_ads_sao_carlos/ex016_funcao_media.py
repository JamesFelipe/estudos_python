"""
Crie uma função que receba como parâmetro uma lista com valores numéricos e retorne a média
desses valores. 
"""
def media(lista):
    media = sum(lista) / len(lista)
    return f'A média dos valores da lista é: {media}'

print(media([10, 10, 10, 10]))
