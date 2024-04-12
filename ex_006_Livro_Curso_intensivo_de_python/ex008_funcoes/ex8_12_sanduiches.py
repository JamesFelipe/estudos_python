def sanduiche(lista):
    ingredientes = []
    for l in lista:
        ingredientes.append(l)
    return f'Os ingredientes do seu sanduíche é: {ingredientes}'


sanduba_ingredientes = ['alface', 'bacon', 'salciha']
sanduba_ingredientes2 = ['Pão']
sanduba_ingredientes3 = ['Pão, Alface, Carne', 'Queijo', 'Tomate', 'Maionese', 'Ovo']
print(sanduiche(sanduba_ingredientes))
print(sanduiche(sanduba_ingredientes2))
print(sanduiche(sanduba_ingredientes3))
