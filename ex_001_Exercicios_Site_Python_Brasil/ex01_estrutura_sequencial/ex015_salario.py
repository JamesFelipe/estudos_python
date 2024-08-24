"""
Faça um Programa que pergunte quanto
você ganha por hora e o número de horas trabalhadas no mês. 

Calcule e mostre o total do seu salário no referido mês, 
sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
"""
ganho_hora = float(input('Digite quanto você ganha por hora R$: '))
horas_trabalhadas = float(input('Digite quantas horas você trabalhou no mês: '))
sal_bruto = ganho_hora * horas_trabalhadas
print(f'Salário bruto: {sal_bruto:.2f}R$')
desconto_ir = sal_bruto * (11/100)
print(f'Foi descontado para o IR: {desconto_ir:.2f}R$')
desconto_inss = sal_bruto * (8 / 100)
print(f'Foi descontado para o INSS: {desconto_inss}R$')
desconto_sindicato = sal_bruto * (5/100)
print(f'Foi descontado para o sindicato: {desconto_sindicato:.2f}R$')
sal_liquido = sal_bruto - (desconto_ir + desconto_inss + desconto_sindicato)
print(f'Somando todos os descontos seu salário líquido é: {sal_liquido:.2f}')
