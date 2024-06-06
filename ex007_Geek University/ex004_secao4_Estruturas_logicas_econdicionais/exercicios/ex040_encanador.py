"""
Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa que solicite
o número de dias trabalhados pelo encanador e imprima a quantia líquida que deverá ser
paga, sabendo-se que são descontados 8% para imposto de renda.
"""
dias_trabalhados = float(input('Digite quantos dias você trabalhou: ')) * 30 # calcula quanto recebeu diretamente
desconto = dias_trabalhados - (dias_trabalhados * 8/100)
print(f'Com desconto de 8% você irá receber líquidos {desconto:.2f} R$')
