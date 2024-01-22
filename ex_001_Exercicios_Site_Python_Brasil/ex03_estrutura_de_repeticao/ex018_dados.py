# Faça um programa que, dado um conjunto de N números,
# determine o menor valor, o maior valor e a soma dos valores.
n = int(input('Digite quantas valores você quer adicionar: '))
numeros = []
for i in range(1, n + 1):
    numero =int (input(f'Digite o {i}º valor: '))
    numeros.append(numero)

print(f'O menor valor é o número: {min(numeros)}')
print(f'O maior valor é o número: {max(numeros)}')
print(f'A soma dos valores digitados é: {sum(numeros)}')
