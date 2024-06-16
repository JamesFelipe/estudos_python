"""
Faça um programa que gera um número aleatório de 1 a 1000. 
O usuário deve tentar acertar qual o número foi gerado, 
a cada tentativa o programa deverá informar 
se o chute é menor ou maior que o número gerado. 

O programa acaba quando o usuário acerta o número gerado. 
O programa deve informar em quantas tentativas o número foi descoberto.
"""
from random import randint
cont_jogadas = 1
numero_aleatorio = randint(1, 1_001)

while True:
    numero_usuario = int(input("Digite um número entre 1 e 1000: "))
    if numero_usuario < numero_aleatorio:
        print('Estou pensando em um número maior...')
    elif numero_usuario > numero_aleatorio:
        print("Estou pensando em um número menor...")
    elif numero_aleatorio == numero_usuario:
        print(f"Parabéns, eu realmente estava pensando no número: {numero_aleatorio}")
        break
    cont_jogadas += 1
print(f'Você venceu com {cont_jogadas} rodadas')
