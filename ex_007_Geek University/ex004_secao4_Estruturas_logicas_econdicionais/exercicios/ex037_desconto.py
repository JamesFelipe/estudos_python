"""
Façaum programa que leia o valor de um produto e imprima o valor com desconto, tendo
em vista que o desconto foi de 12%
"""
valor_produtor = float(input('Digite o valor do produto: '))
print(f'Com 12% de desconto você vai pagar: {valor_produtor - (valor_produtor * 12 / 100)}')
