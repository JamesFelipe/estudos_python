# Faça um programa que some todos os números naturais abaixo de 1000 que são múltiplos de 3 ou 5.
print("Os múltiplos de 3 e 5 são: ")
for i in range(0, 1001):
    if (i % 3 == 0 and i % 5 == 0):
        print(i, end=" ")
