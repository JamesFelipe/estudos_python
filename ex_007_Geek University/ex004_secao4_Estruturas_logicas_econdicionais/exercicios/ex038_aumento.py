"""
Leia o salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo que
ele recebeu um aumento de 25%.
"""
salario = float(input('Digite seu salário atual: '))
print(f'Com aumento de 25% seu novo salário será de {salario + (salario * 25 /100)}')
