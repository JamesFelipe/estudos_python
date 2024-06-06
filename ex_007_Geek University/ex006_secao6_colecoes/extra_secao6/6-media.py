print('Digite 10 valores: ')
soma = 0
for i in range(1, 11):
    valores = int(input(f'Digite o valor{i}: '))
    soma += valores
    media = soma / 10

print(f'A média dos valores digitados é: {media}')
