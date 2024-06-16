"""
Leia um vetor com 10 números reais, ordene os elementos deste vetor, 
e no final escreva os elementos do vetor ordenado.
"""
numeros = []
for i in range(1, 11):
    numero = float(input('Digite valores com pontos flutuantes: '))
    numeros.append(numero)
    
numeros.sort()
print(f'Valores ordenados: {numeros}')
