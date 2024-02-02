"""
Escreva um programa que receba o salário de um funcionário (float), e retorne o resultado do
novo salário com reajuste de 35%.
"""
salario = float(input('Digite o seu salário: '))
novo_valor = salario + (salario * 35/100)
print(f'Com reajuste de 35% seu novo salário será de {novo_valor:.2f}R$')
