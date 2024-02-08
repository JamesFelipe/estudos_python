"""
Implemente a opção de o usuário iniciar uma nova partida. 
Ao finalizar uma rodada, após o resultado final, 
o jogo deve perguntar se o jogador quer iniciar uma nova partida e, em caso negativo, encerrar a aplicação
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
            continua = input('Você quer continuar jogando[Sim/Nao]: ').strip().lower()
            if continua == 's':
                try:
                    numero = int(input('Digite um valor inteiro: '))
                    cont += 1
                    if numero == aleatorio:
                        print(f'Parabéns, eu realmente estava pensando no {numero}')
                        if cont == 1:
                            print('Pontuação final: 100 pontos')
                        elif cont == 5:
                            print('Pontuação final: 10 pontos')
                except ValueError:
                    print('Digite um valor válido')
            elif continua == 'n':
                print('Programa encerrado...')
                break
    except ValueError:
        print('Digite um valor válido')
else:
    print('Pontuação final: 0 pontos')
