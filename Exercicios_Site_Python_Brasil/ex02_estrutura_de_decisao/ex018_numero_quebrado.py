"""
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:

326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""
numero = int(input('Digite um valor menor que 1000: '))
centena = numero % 1_000 // 100
dezena = numero % 100 // 10
unidade = numero % 10

if int(numero) >= 1000:
    print(f'{numero} maior ou igual a 1000')
else:
    if centena > 1:
     print(f'{centena} Centenas')
    else:
        print(f'{centena} Centena')
    if centena > 1:
        print(f'{dezena} Dezenas')
    else:
        print(f'{dezena} Dezena')
    if unidade > 1:
        print(f'{unidade} Unidades')
    else:
        print(f'{unidade} Unidade')    