"""
Faça um Programa que leia um número inteiro menor que 1000
e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. 
Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com:
326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""
n = int(input('Digite um valor inteiro de 0 a 9999: '))
if n <= 999:
    unidade = n % 10
    dezena = n % 100 // 10
    centena = n % 1_000 // 100
    print('Centena: ', centena)
    print('Dezena: ', dezena)
    print('Unidade: ', unidade)
