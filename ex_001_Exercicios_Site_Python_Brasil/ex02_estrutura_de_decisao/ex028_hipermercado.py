"""
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. 
Confira:

                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes,
cada cliente poderá levar apenas um dos tipos de carne da promoção,
porém não há limites para a quantidade de carne por cliente.

Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de
5% sobre o total da compra.

Escreva um programa que peça o tipo e a quantidade de carne comprada pelo
usuário e gere um cupom fiscal,
contendo as informações da compra: tipo e quantidade de carne, preço total,
tipo de pagamento, valor do desconto e valor a pagar.
"""
tipo = input('Digite o tipo da carne: ').strip().lower()
qtd_carne = float(input('Digite a quantidade da carne: '))
tipo_de_pagamento = int(input('[1] - Cartão Tabajara - [2] - Outros: '))

if tipo == 'file duplo' and qtd_carne <= 5 and tipo_de_pagamento == 2:
    preco_file = qtd_carne * 4.90
    print(f'''
Cupom Fiscal
Tipo da carne: {tipo}
Quantidade: {qtd_carne}
Tipo de Pagamento: Outros
Valor do desconto:0%
Preço Total: {preco_file:.2f}''')

elif tipo == 'alcatra' and qtd_carne <= 5 and tipo_de_pagamento == 2:
    preco_alcatra = qtd_carne * 5.90
    print(f'''
Cupom Fiscal
Tipo da carne: {tipo}
Quantidade: {qtd_carne}
Tipo de Pagamento: Outros
Valor do desconto:0%
Preço Total: {preco_alcatra:.2f}''')
elif tipo == 'picanha' and qtd_carne <= 5 and tipo_de_pagamento == 2:
    preco_picanha = qtd_carne * 6.90
    print(f'''
Cupom Fiscal
Tipo da carne: {tipo}
Quantidade: {qtd_carne}
Tipo de Pagamento: Outros
Valor do desconto:0%
Preço Total: {preco_picanha:.2f}''')
    
if tipo == 'file duplo' and qtd_carne >= 5 and tipo_de_pagamento == 2:
    preco_file = qtd_carne * 5.80
    print(f'''
Cupom Fiscal
Tipo da carne: {tipo}
Quantidade: {qtd_carne}
Tipo de Pagamento: Outros
Valor do desconto:0%
Preço Total: {preco_file:.2f}''')
elif tipo == 'alcatra' and qtd_carne >= 5 and tipo_de_pagamento == 2:
    preco_alcatra = qtd_carne * 6.80
    print(f'''
Cupom Fiscal
Tipo da carne: {tipo}
Quantidade: {qtd_carne}
Tipo de Pagamento: Outros
Valor do desconto:0%
Preço Total: {preco_alcatra:.2f}''')
elif tipo == 'picanha' and qtd_carne >= 5 and tipo_de_pagamento == 2:
    preco_picanha = qtd_carne * 7.80
    print(f'''
Cupom Fiscal
Tipo da carne: {tipo}
Quantidade: {qtd_carne}
Tipo de Pagamento: Outros
Valor do desconto:0%
Preço Total: {preco_picanha:.2f}''')
    
# Cartão Tabajara
if tipo == 'file duplo' and qtd_carne <= 5 and tipo_de_pagamento == 1:
    preco_file = qtd_carne * 4.90
    desconto = preco_file - (preco_file * 5/100)
    print(f'''
Cupom Fiscal
Tipo da carne: {tipo}
Quantidade: {qtd_carne}
Tipo de Pagamento:Cartão Tabajara
Valor do desconto: 5%
Preço Total: {desconto:.2f}''')

elif tipo == 'alcatra' and qtd_carne <= 5 and tipo_de_pagamento == 1:
    preco_alcatra = qtd_carne * 5.90
    desconto = preco_alcatra - (preco_alcatra * 5/100)
    print(f'''
Cupom Fiscal
Tipo da carne: {tipo}
Quantidade: {qtd_carne}
Tipo de Pagamento: Cartão Tabajara
Valor do desconto:5%
Preço Total: {desconto:.2f}''')
elif tipo == 'picanha' and qtd_carne <= 5 and tipo_de_pagamento == 1:
    preco_picanha = qtd_carne * 6.90
    desconto = preco_picanha - (preco_picanha * 5/100)
    print(f'''
Cupom Fiscal
Tipo da carne: {tipo}
Quantidade: {qtd_carne}
Tipo de Pagamento: Cartão Tabajara
Valor do desconto: 5%
Preço Total: {desconto:.2f}''')

if tipo == 'file duplo' and qtd_carne >= 5 and tipo_de_pagamento == 1:
    preco_file = qtd_carne * 5.80
    desconto = preco_file - (preco_file * 5/100)
    print(f'''
Cupom Fiscal
Tipo da carne: {tipo}
Quantidade: {qtd_carne}
Tipo de Pagamento: Cartão Tabajara
Valor do desconto: 5%
Preço Total: {desconto:.2f}''')
elif tipo == 'alcatra' and qtd_carne >= 5 and tipo_de_pagamento == 1:
    preco_alcatra = qtd_carne * 6.80
    desconto = preco_alcatra - (preco_alcatra * 5/100)
    print(f'''
Cupom Fiscal
Tipo da carne: {tipo}
Quantidade: {qtd_carne}
Tipo de Pagamento: Cartão Tabajara
Valor do desconto: 5%
Preço Total: {desconto:.2f}''')
elif tipo == 'picanha' and qtd_carne >= 5 and tipo_de_pagamento == 2:
    preco_picanha = qtd_carne * 7.80
    desconto = preco_picanha - (preco_picanha * 5/100)
    print(f'''
Cupom Fiscal
Tipo da carne: {tipo}
Quantidade: {qtd_carne}
Tipo de Pagamento: Cartão Tabajara
Valor do desconto:5%
Preço Total: {desconto:.2f}''')
