# Faca um algoritmo que leia um número positivo e imprima seus divisores.
numero = int(input("Digite um valor inteiro: "))
print(f'Os divisores de {numero} são: ')
for i in range(1, numero + 1):
    if numero % i == 0:
        print(i, end=" ")
