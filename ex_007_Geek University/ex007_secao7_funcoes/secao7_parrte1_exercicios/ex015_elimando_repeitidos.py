"""
Leia um vetor com 20 números inteiros. 

Escreva os elementos do vetor eliminando elementos repetidos.
"""
numeros = []
for i in range(1, 21):
    numero = int(input("Digite um valor inteiro: "))
    numeros.append(numero)
    
print(set(numeros))
