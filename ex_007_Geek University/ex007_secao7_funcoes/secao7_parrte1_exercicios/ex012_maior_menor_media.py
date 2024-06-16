"""
Fazer um programa para ler 5 valores e, em seguida, mostrar todos os valores lidos
juntamente com o maior, o menor e a média dos valores.
"""
numeros = []
for x in range(1, 6):
    numero = int(input(f'Digite o {x}º número: '))
    numeros.append(numero)  

print(f'Os valores lidos são: {numeros}')
print(f'O maior valor lido foi: {max(numeros)}')
print(f'O menor número digitado foi: {min(numeros)}')
print(f'A média dos valores digitados é: {sum(numeros) / len(numeros)}')
