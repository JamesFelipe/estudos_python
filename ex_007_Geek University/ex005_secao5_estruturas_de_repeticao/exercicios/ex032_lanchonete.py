"""
Escrever um programa que leia o código do produto escolhido do cardápio de uma lan-
chonete e a quantidade. O programa deve calcular o valor a ser pago por aquele lanche.
Considere que a cada execução somente será calculado um pedido. O cardápio da lan-
chonete segue o padrão abaixo:

Especificação       | Código | Preço
                    |         
Cachorro Quente     | 100    |1.20
Bauru Simples       | 101    |1.30
Bauru com Ovo       | 102    |1.50
Hamburguer          | 103    |1.20
Cheeseburguer       | 104    |1.70
Suco                | 105    |2.20
Refrigerante        | 106    |1.00)


"""
codigo = int(input('Digite o código do produto: '))
quantidade = int(input('Digite a quantidade do produto: '))
match codigo:
    case 100:
        print('\nProduto Selecionado: Cachorro Quente')
        print(f'Quantidade: {quantidade}\nPreço Total: {quantidade * 1.20:.2f} R$')
    case 101:
        print('\nProduto Selecionado: Bauru Simples')
        print(f'Quantidade: {quantidade}\nPreço Total: {quantidade * 1.30:.2f} R$')
    case 102:
        print('\nProduto Selecionado: Bauru com Ovo')
        print(f'Quantidade: {quantidade}\nPreço Total: {quantidade * 1.50:.2f} R$')
    case 103:
        print('\nProduto Selecionado: Hamburguer')
        print(f'Quantidade: {quantidade}\nPreço Total: {quantidade * 1.20:.2f} R$')
    case 104:
        print('\nProduto Selecionado: Cheesburguer')
        print(f'Quantidade: {quantidade}\nPreço Total: {quantidade * 1.70:.2f} R$')
    case 105:
        print('\nProduto Selecionado: Suco')
        print(f'Quantidade: {quantidade}\nPreço Total: {quantidade * 2.20:.2f} R$')
    case 106:
        print('\nProduto Selecionado: Refrigerante')
        print(f'Quantidade: {quantidade}\nPreço Total: {quantidade * 1.00:.2f} R$')
    case _:
        print('Valor inválido')
