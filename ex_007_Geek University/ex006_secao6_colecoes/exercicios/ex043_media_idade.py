"""
Faça um programa que leia um número indeterminado de idades de indivíduos 
(pare quando for informada a idade 0), e calcule a idade média desse grupo.
"""
soma = cont = media = 0
while True:
    idades = int(input("Digite uma idade[0 para sair]: "))
    if idades == 0:
        break
    else:
        cont += 1
        soma += idades
        media = soma / cont
print(f'A média das idades digitadas é: {media}')
