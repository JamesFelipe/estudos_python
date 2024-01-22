"""
Faça um programa para o cálculo de uma folha de pagamento, 
sabendo que os descontos são do Imposto de Renda, 
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, 
mas não é descontado (é a empresa que deposita). 

O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%

Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, 
dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
"""

# Código Bard
def calcula_folha_pagamento(valor_hora, quantidade_horas):
    salario_bruto = valor_hora * quantidade_horas
    desconto_ir = 0
    if salario_bruto <= 900:
        desconto_ir = 0
    elif salario_bruto <= 1500:
        desconto_ir = salario_bruto * 0.05
    elif salario_bruto <= 2500:
        desconto_ir = salario_bruto * 0.1
    else:
        desconto_ir = salario_bruto * 0.2
    desconto_sindicato = salario_bruto * 0.03
    salario_liquido = salario_bruto - desconto_ir - desconto_sindicato
    return salario_bruto, desconto_ir, desconto_sindicato, salario_liquido


valor_hora = float(input("Valor da hora: "))
quantidade_horas = int(input("Quantidade de horas: "))

salario_bruto, desconto_ir, desconto_sindicato, salario_liquido = calcula_folha_pagamento(valor_hora, quantidade_horas)

print("Valor da hora:", valor_hora)
print("Quantidade de horas:", quantidade_horas)
print("Salário Bruto:", salario_bruto)
print("Desconto do IR:", desconto_ir)
print("Desconto do Sindicato:", desconto_sindicato)
print("Salário Líquido:", salario_liquido)
