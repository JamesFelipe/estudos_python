"""
Leia um valor em real e a cotação do dólar. Em seguida, imprima o valor correspondente
em dólares.
"""
real = float(input('Digite quantos reais você tem atualmente: '))
cotacao_dolar = float(input('Digite a cotação do dolar hoje: '))
print(f'Com {real} R$ você pode comprar {real / cotacao_dolar:.2f} US$')
