"""
Recebao salário-base de um funcionário. Calcule e imprima o salário a receber, sabendo
se que esse funcionário tem uma gratificação de 5% sobre o salário-base. Além disso,
ele paga 7% de imposta sobre o salário-base.
"""
salario_base = float(input('Digite o valor do seu salário base: '))
gratificao = salario_base * 0.05
imposto = salario_base - (salario_base * 7/100)
total = imposto - gratificao
print(f'Com gratificação de 5% e imposto de 7% você irá receber: {total:.2f} R$')
