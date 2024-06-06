from random import randint

i = acertos = 0
a = b = soma = resp = 0

for i in range(0, 5):
    a = (randint(1, 100) % 100) + 1
    b = (randint(1, 100) % 100) + 1
    soma = a + b
    
    #resp = soma
    resp = int(input((f'Qual é a soma de {a} + {b}? ')))
    if resp != soma:
        print(f'Respota errada. A resposta certa é: {soma}')
    else:
        acertos += 1
print(f'Você acertou {acertos} vezes')
