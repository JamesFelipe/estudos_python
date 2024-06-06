print("""           Cardapio

----------------------------------
|Código|     Produto     | preço |         
----------------------------------
| 100  | Cachorro Quente | 1.20  | 
| 101  | Bauru Simples   | 1.30  |
| 102  | Bauru com ovo   | 1.50  |
| 103  | Hamburguer      | 1.20  |
| 104  | Cheesburguer    | 1.70  |
| 105  | Suco            | 2.20  | 
| 106  | refrigerante    | 1.00  |
----------------------------------""")

cod = int(input('Digite o código do produto: '))
qtd = int(input('Digite a quantidade do produto: '))
if cod == 100:
    preco = 1.20
    print(f'Você irá pagar R$ {preco * qtd:.2f} por {qtd} Cachorro(s) quente(s)')
elif cod == 101:
    preco = 1.30
    print(f'Você irá pagar R$ {preco * qtd:.2f} por {qtd} de Bauru(s) simples')
elif cod == 102:
    preco = 1.50
    print(f'Você irá pagar R$ {preco * qtd:.2f} por {qtd} Bauru(s) com ovo')
elif cod == 103:
    preco = 1.20
    print(f'Você irá pagar R$ {preco * qtd:.2f} por {qtd} Hamburguer(s)')
elif cod == 104:
    preco = 1.70
    print(f'Você irá pagar R$ {preco * qtd:.2f} por {qtd} Cheesburguer(s)')
elif cod == 105:
    preco = 2.20
    print(f'Você irá pagar R$ {preco * qtd:.2f} por {qtd} suco(s)')
elif cod == 106:
    preco = 1.00
    print(f'Você irá pagar R$ {preco * qtd:.2f} por {qtd} refrigerante(s)')
else:
    print('Código Inválido... Produto não encontrado')
