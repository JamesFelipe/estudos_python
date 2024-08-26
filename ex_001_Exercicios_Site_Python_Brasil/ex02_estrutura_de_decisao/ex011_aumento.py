"""
As Organizações Tabajara resolveram dar um aumento de salário
aos seus colaboradores e lhe contraram para desenvolver
o programa que calculará os reajustes.

Faça um programa que recebe o salário de um colaborador
e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado,
informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
"""
salario = float(input('Digite seu salário atual: '))
if salario <= 280:
    aumento = salario + (salario * 20/100)
    print(f'Salário antigo: {salario:.2f} \
- Salário com 20% de aumento: {aumento:.2f}')

elif salario > 280 and salario <= 700:
    aumento = salario + (salario * 15/100)
    print(f'Salário antigo: {salario:.2f} \
- Salário com 15% de aumento: {aumento:.2f}')

elif salario > 700 and salario <= 1500:
    aumento = salario + (salario * 10/100)
    print(f'Salário antigo: {salario:.2f} \
- Salário com 10% de aumento: {aumento:.2f}')

elif salario > 1500:
    aumento = salario + (salario * 5/100)
    print(f'Salário antigo: {salario:.2f} \
- Salário com 5% de aumento: {aumento:.2f}')
