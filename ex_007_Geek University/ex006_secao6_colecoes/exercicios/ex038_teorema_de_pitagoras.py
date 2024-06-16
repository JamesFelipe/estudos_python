"""
Faça um programa que calcule o terno pitagórico a, b, c, 
para o qual a + b + c= 1000. 

Um terno pitagórico é um conjunto de três números naturais, a, b, c, 
para a qual, Por exemplo, a² + b² = c² -> 3² + 4² = 9 +16 = 25 = 5²

"""
# Código ChatGpt
def encontrar_triplas():
    triplas = []

    # Itera sobre possíveis valores de a, b e c
    for a in range(1, 32):  # 32^2 > 1000, então não precisamos ir além disso
        for b in range(a, 32):  # b começa em a para evitar duplicidade de combinações
            for c in range(b, 32):  # c começa em b pelo mesmo motivo
                if a**2 + b**2 + c**2 == 1000:
                    triplas.append((a, b, c))

    return triplas

# Executando a função e imprimindo os resultados
triplas = encontrar_triplas()
for tripla in triplas:
    print(tripla)
