"""
Leia um número positivo do usuário, então, 
calcule e imprima a sequência Fibonacci até o primeiro número superior ao número lido. 
Exemplo: se o usuário informou o número 30, a sequência a ser impressa será 0 1 1 235 8 13 21 34.
"""
# Código Chatgpt modificado
n = int(input('Informe um número positivo: '))
t1 = 0
t2 = 1
print('Sequência de Fibonacci:', end=' ')
print(f'{t1} {t2}', end=' ')

while True:
    t3 = t1 + t2
    if t3 > n:
        print(f'{t3}', end=' ')
        break
    print(f'{t3}', end=' ')
    t1 = t2
    t2 = t3
