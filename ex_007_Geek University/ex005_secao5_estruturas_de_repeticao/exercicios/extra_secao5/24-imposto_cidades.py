valor = float(input('Digite o valor do produto: '))
estado = input('Para qual estado vai o produto (Digite a sigla do estado): ').strip().lower()

if estado == 'mg':
    imposto = valor + (valor * 7/100)
    print(f'Para Minas Gerais o valor total fica em R$: {imposto}')
elif estado == 'sp':
    imposto = valor + (valor * 12/100)
    print(f'Para São Paulo o valor total fica em R$: {imposto}')
elif estado == 'rj':
    imposto = valor + (valor * 15/100)
    print(f'Para o Rio de Janeiro o valor total fica em R$: {imposto}')
elif estado == 'ms':
    imposto = valor + (valor * 8/100)
    print(f'Para Mato Grosso do Sul o valor total fica em R$: {imposto}')
else:
    print('Error')
