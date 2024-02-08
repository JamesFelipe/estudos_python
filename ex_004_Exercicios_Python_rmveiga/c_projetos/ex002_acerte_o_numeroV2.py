"""
Implemente um sistema de pontuação com o seguinte comportamento: 
se o usuário adivinhar o número na primeira tentativa, 
receberá a pontuação máxima (ex. 100 pontos);

se o usuário adivinhar o número na última tentativa, 
receberá a pontuação mínima (ex. 10 pontos); 

se o usuário não acertar o número, não receberá nenhum ponto.
"""
from random import randint
aleatorio = randint(1, 11)
print('Estou pensando em um número entre 1 e 10, tente adivinhar qual: ')

n = cont = 0
while n < 5:
    numero = int(input('Digite um numero: '))
    cont += 1
    if numero == aleatorio:
        print(f'Parabéns, eu realmente estava pensando no {numero}')
        if cont == 1:
            print('Pontuação final: 100 pontos')
        elif cont == 5:
            print('Pontuação final: 10 pontos')
        break
else:
    print('Pontuação final: 0 pontos')