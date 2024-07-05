# Pares, sem o zero
numeros = list(range(101))
pares = []
for numero in numeros:
    if numero % 2 == 0 and numero != 0:
       pares.append(numero)
print(pares)


# ímpares
numeros = list(range(101))
impares = []
for numero in numeros:
    if numero % 2 == 1 and numero != 0:
       impares.append(numero)
print(impares)
