preco = float(input('Digite o preço antigo do produto: '))

if preco <= 50:
    preco_novo = preco + (preco * 5 / 100)
elif preco > 50 and preco <= 100:
    preco_novo = preco + (preco * 10 / 100)
elif preco > 100:
    preco_novo = preco + (preco * 15 / 100)
    
if preco_novo <= 80:
    print(f'Preço R${preco_novo}. Barato!')
elif preco_novo > 80 and preco_novo < 120:
    print(f'Preço R${preco_novo}. Normal!')
elif preco_novo > 120 and preco_novo < 200:
    print(f'Preço R${preco_novo}. Caro!')
elif preco_novo > 200:
    print(f'Preço R${preco_novo}. Muito caro')
