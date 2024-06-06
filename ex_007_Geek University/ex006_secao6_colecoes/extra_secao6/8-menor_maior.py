maximo = minimo = 0
print('Digite 10 valores inteiros: ')
for p in range(1, 11):
    valores = int(input(f'Valor{p}: '))
    if p == 1:
        maximo = valores
        minimo = valores
    else:
        if valores > maximo:
            maximo = valores
        if valores < minimo:
            minimo = valores
print(f'O maior valor lido foi {maximo}Kg')
print(f'O menor valor lido foi {minimo}Kg')
