"""
Dados três valores: A, B, C, verificar se eles podem ser valores dos lados de um triângulo
e, se forem,
    se é um triângulo escaleno, equilátero ou isóscele, considerando os seguin-
tes conceitos:

     O comprimento de cada lado do um triângulo é menor do que a soma dos outros dois lados.
     Chama-se equilátero
     
     o triângulo que tem trôs lados iguais.
     Denominam-so isósceles o triângulo que tem o comprimento de dois lados iguais.
     Recebe o nome de escaleno o triângulo que tem os três lados diferentes.
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
