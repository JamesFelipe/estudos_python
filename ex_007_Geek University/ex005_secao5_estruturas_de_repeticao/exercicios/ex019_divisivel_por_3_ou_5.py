"""
Faça um programa para verificar se um determinado número inteiro e divisível por 3 ou
5, mas não simultaneamente pelos dois.
"""
numero = int(input('Digite um valor inteiro: '))
if numero % 5 == 0 or numero % 5 == 5:
    print('Número Dívisivel por 5')
else:
    print('Número Não divisivel por 5')


soma = 0
if numero > 0:
    numero2 = str(numero)
    for i in range(0, len(numero2)):
        soma += int(numero2[i])
if soma % 3 == 0:
    print('O número é divisivel por 3')
else:
    print('O número não é divisivel por 3')
