"""
Desenvolva um jogo de acerte o número, onde o computador escolhe um número inteiro aleatório de 0 a 10, 
e o usuário tem 5 tentativas para adivinhar o número
OBS.: O design da tela pode ser implementado livremente
"""
from random import randint
aleatorio = randint(1, 11)
print('Estou pensando em um número entre 1 e 10, tente adivinhar qual: ')

n = 0
while n < 5:
    numero = int(input('Digite um numero: '))
    if numero == aleatorio:
        print(f'Parabéns, eu realmente estaa pensando no {numero}')
        break
    else:
        print('Você errou')
