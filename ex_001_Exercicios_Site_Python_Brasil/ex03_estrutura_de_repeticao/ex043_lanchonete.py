"""
O cardápio de uma lanchonete é o seguinte:

Especificação       Código  Preço
Cachorro Quente     100     R$ 1,20 X
Bauru Simples       101     R$ 1,30 X
Bauru com ovo       102     R$ 1,50 X
Hambúrguer          103     R$ 1,20 X
Cheeseburguer       104     R$ 1,30 X
Refrigerante        105     R$ 1,00

Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. 
Considere que o cliente deve informar quando o pedido deve ser encerrado.
"""
total_geral = []
while True:
    print(f'''
Especificação\t\tCódigo\t\tPreço
Cachorro Quante\t\t100\t\tR$ 1,20
Bauru Simples\t\t101\t\tR$ 1,30
Bauru com ovo\t\t102\t\tR$ 1,50
Hambúrguer\t\t103\t\tR$ 1,20
Cheesburguer\t\t104\t\tR$ 1,30
Refrigerante\t\t105\t\tR$ 1,00''')
    codigo = int(input('Digite o código do item: '))
    qtd = int(input('Digite a quantidade: '))
    match codigo:
        case 100:
            total = qtd * 1.20
            print(f'Comprando {qtd} Cachorros quentes você vai pagar: R${total:.2f}')
        case 101:
            total = qtd * 1.30
            print(f'Comprando {qtd} Bauru Simples você vai pagar: R${total:.2f}')
        case 102:
            total = qtd * 1.50
            print(f'Comprando {qtd} Cachorros quentes você vai pagar: R${total:.2f}')
        case 103:
            total = qtd * 1.20
            print(f'Comprando {qtd} Cachorros quentes você vai pagar: R${total:.2f}')
        case 104:
            total = qtd * 1.30
            print(f'Comprando {qtd} Cachorros quentes você vai pagar: R${total:.2f}')
        case 105:
            total = qtd * 1.00
            print(f'Comprando {qtd} Cachorros quentes você vai pagar: R${total:.2f}')
        case _:
            print('Valor inválido')
    total_geral.append(total)
    opcao = input('Você quer continuar[Sim/Não]: ').strip().lower()[0]
    if opcao == 'n':
        break
print(f'A sua conta geral será de R${sum(total_geral):.2f}')

