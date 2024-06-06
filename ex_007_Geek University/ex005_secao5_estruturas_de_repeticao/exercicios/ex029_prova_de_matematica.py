"""
Faça uma prova de matemática para crianças que estão aprendendo a somar números
inteiros menores do que 100. Escolha números aleatórios entre 1 e 100, e mostre na
tela a pergunta: qual é a soma de a + b, onde a e b são os números aleatórios. Peça a
resposta. Faça cinco perguntas ao aluno, e mostre para ele as perguntas e as respostas
corretas, além de quantas vezes o aluno acertou.
"""
from random import choice
numeros = list(range(1, 99))
cont_acerto = cont_erro = 0
for i in range(5):
    a = choice(numeros)
    b = choice(numeros)
    print(f'{a} + {b} = ')
    conta = int(input('Digite sua resposta: '))
    print(f'Gabarito: {a + b}')
    if conta == a + b:
        cont_acerto += 1
    else:
        cont_erro += 1

print(f'Você Acertou {cont_acerto} vezes e errou {cont_erro} vezes')
