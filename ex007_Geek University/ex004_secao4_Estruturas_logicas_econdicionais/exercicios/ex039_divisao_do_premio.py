"""
A importância de R$ 780.000,00 será dividida entre três ganhadores de um concurso.
Sendo que da quantia total:

    O primeiro ganhador receberá 46%;
    O segundo receberá 32%;
    O terceiro receberá o restante;
    
Calcule e imprima a quantia ganha por cada um dos ganhadores.
"""
total = 780_000.00
primeiro = total * 0.46
segundo = total * 0.32
terceirio = total - (primeiro + segundo)
print(f'O primeiro ganhador ficará com {primeiro:.2f} R$')
print(f'O segundo ganhador ficará com {segundo:.2f} R$')
print(f'O terceirio ganhador ficará com {terceirio:.2f} R$')
