"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores 
e lhe contraram para desenvolver o programa que calculará os reajustes.

Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste; 
o percentual de aumento aplicado; 
o valor do aumento; 
o novo salário, após o aumento. 
"""
salario = float(input('Digite aqui o seu salário: '))
if salario <= 280:
    aumento_20 = salario + (salario * 20 / 100)
    print(f'Salário atual: {salario}')
    print(f'Com 20% de aumento, você passará a receber {aumento_20:.2f}')
    acrescimo = salario * 0.2
    print(f'No total foram acrescidos ao seu salário {acrescimo:.2f} R$')
    
elif salario > 280 and salario <= 700:
    aumento_15 = salario + (salario * 15 / 100)
    print(f'Salário atual: {salario}')
    print(f'Com 15% de aumento, você passará a receber {aumento_15:.2f}')
    acrescimo = salario * 0.15
    print(f'No total foram acrescidos ao seu salário {acrescimo:.2f} R$')
    
elif salario > 700 and salario <= 1500:
    aumento_10 = salario + (salario * 10 / 100)
    print(f'Salário atual: {salario}')
    print(f'Com 10% de aumento, você passará a receber {aumento_10:.2f}')
    acrescimo = salario * 0.10
    print(f'No total foram acrescidos ao seu salário {acrescimo:.2f} R$')