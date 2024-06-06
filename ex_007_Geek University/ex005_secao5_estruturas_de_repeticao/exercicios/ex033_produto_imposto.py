"""
Um produto vai sofrer aumento de acordo com a tabela abaixo.  Leia o preço antigo,
calcule e escreva o preço novo, e escreva uma mensagem em função do preço novo (de
acordo com à segunda tabela).
_____________________________________________________      ____________________________________________________________
|  Preço antigo         |   Percentural de Aumento  |      | Preço Novo                              |  Mensagem      |
|   Até R$ 50           |           5%              |      |  Até R$ 80, 00                          |   Barato       |
|   Entre R$ 50 e 100   |           10%             |      |  entre R$ 80 e R$ 120 (inclusive)       |   Normal       |
|   Acima de R$ 100     |           15%             |      |  entre R$ 120 e R$ 200 (inclusive)      |   Caro         |
-----------------------------------------------------      |  Acima de R$ 200                        |   Muito Caro   |
                                                           =-----------------------------------------------------------

"""

preco_antigo = float(input('Digite o preço do produto: '))
if preco_antigo <= 50:
    preco_novo = preco_antigo + (preco_antigo * 5 / 100)
    print(f'Novo preço: {preco_novo:.2f}')
elif preco_antigo > 50 and preco_antigo <= 100:
    preco_novo = preco_antigo + (preco_antigo * 10 / 100)
    print(f'Novo preço: {preco_novo:.2f}')
elif preco_antigo > 100:
    preco_novo = preco_antigo + (preco_antigo * 15 / 100)
    print(f'Novo preço: {preco_novo:.2f}')
    
if preco_novo <= 80:
    print('barato')
elif preco_novo > 80 and preco_novo <= 120:
    print('Normal')
elif preco_novo > 120 and preco_novo <= 200:
    print('Caro')
elif preco_novo > 200:
    print('Muito Caro')
