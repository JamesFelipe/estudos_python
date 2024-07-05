# jogo de adivinhação
from random import randint
aleatorio = randint(1, 5)

while True:
    jogador = int(input("Digite o valor que você acha que estou pensando: "))
    if aleatorio == jogador:
        print("Parabéns, eu realmente está pensando no: ", aleatorio)
        break
    else:
        if jogador < aleatorio:
            print("Eu estava pensando em um valor maior: ")
        else:
            print("Eu estava pensando em um valor menor: ")
