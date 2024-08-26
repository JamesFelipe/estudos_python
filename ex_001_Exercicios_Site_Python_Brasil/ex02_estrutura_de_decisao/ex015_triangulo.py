"""
Faça um Programa que peça os 3 lados de um triângulo. 
O programa deverá informar se os valores podem ser um triângulo. 
Indique, caso os lados formem um triângulo, se o mesmo é: 
equilátero, isósceles ou escaleno.

Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados
for maior que o terceiro;

Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
"""
reta1 = int(input('Digite o valor da primeira reta: '))
reta2 = int(input('Digite o valor da segunda reta: '))
reta3 = int(input('Digite o valor da terceira reta: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('É um triângulo')
    if reta1 != reta2 != reta3:
        print('Triângulo Escaleno')
    elif reta1 == reta2 != reta3 or reta2 == reta1 != reta3 or reta3 == reta2 != reta1:
        print('Triângulo Isósceles')
    else:
        print('Triângulo Equilátero')
else:
    print('Não é um triângulo')