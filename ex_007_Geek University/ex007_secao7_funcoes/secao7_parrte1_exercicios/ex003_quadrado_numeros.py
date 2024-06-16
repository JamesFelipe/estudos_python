"""
Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado das
componentes deste vetor, armazenando o resultado em outro vetor. Os conjuntos têm
10 elementos cada. Imprimir todos os conjuntos.
"""
numeros = []
for i in range(1, 11):
    numero = float(input(f'Digite o {i}º valor: '))
    numeros.append(numero)
quadrado = [x**2 for x in numeros]
print(f'O quadrado dos números são: {quadrado}')
