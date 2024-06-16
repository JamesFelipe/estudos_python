"""
Faça um programa que calcule a área de um triângulo, 
cuja base e altura são fornecidas pelo usuário. 

Esse programa não pode permitir a entrada de dados inválidos, ou seja, 
medidas menores ou iguais a 0.
"""
reta1 = float(input('Digite o comprimento da primeira reta: '))
reta2 = float(input('Digite o comprimento da segunda reta: '))
reta3 = float(input('Digite o comprimento da terceira reta: '))

    
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('É um triângulo')
else:
    print('Não é um triângulo')
