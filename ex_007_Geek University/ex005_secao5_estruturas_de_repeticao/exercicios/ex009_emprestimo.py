"""
Leia o salário do um trabalhador e o valor da prestação do um empréstimo. Se a
prestação for maior que 20% do salário imprima: Enpréstimo não concedido, caso
contrário imprima: Empréstimo concedido.
"""
salario = float(input('Digite seu salário: '))
prestacao = float(input('Digite o valor da prestação: '))
total = salario * 0.20
if prestacao > total:
    print('Empréstimo não concedido')
else:
    print('Empréstimo Concedido')
