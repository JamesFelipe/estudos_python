"""
Implemente um controle de erros.
Caso o jogador digite um número fora da faixa permitida ou caracteres não numéricos, 
o sistema deve notificar o jogador e solicitar o input correto.
"""
from random import randint
aleatorio = randint(1, 10)
print('Estou pensando em um número entre 1 e 10, tente adivinhar qual: ')

n = cont = 0
while n < 5:
    try:
        numero = int(input('Digite um valor inteiro: '))
        cont += 1
        if numero == aleatorio:
            print(f'Parabéns, eu realmente estava pensando no {numero}')
            if cont == 1:
                print('Pontuação final: 100 pontos')
            elif cont == 5:
                print('Pontuação final: 10 pontos')
            break
    except ValueError:
        print('Digite um valor válido')
else:
    print('Pontuação final: 0 pontos')
