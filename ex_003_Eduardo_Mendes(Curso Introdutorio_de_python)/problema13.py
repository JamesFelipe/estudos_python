# Faça um programa que da uma lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] e um número inteiro, 
# imprima a tabuada desse número
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numero = int(input('Digite um número: '))
for i in lista:
    print(f'{i} X {numero} = {i * numero}')
