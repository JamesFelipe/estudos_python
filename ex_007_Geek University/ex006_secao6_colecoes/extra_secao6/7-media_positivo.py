print('Digite 10 valores: ')
soma = 0
for i in range(1, 11):
    valores = int(input(f'Digite o valor{i}: '))
    if valores > 0:
        soma += valores
        media = soma / 10

print(f'A média dos valores positivos digitados é: {media}')
