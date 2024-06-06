print('Digite 10 valores: ')
soma = 0
for i in range(1, 11):
    valores = int(input(f'Digite o valor{i}: '))
    soma += valores

print(f'A soma dos valores digitados é: {soma}')
