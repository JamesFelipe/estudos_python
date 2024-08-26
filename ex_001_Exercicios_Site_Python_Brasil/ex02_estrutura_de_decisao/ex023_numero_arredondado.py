"""
Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
Dica: utilize uma função de arredondamento
"""
# Código Baseado pelo Chatgpt
n = float(input('Digite um número: '))
if n == round(n):
    print(f'{round(n)} é inteiro')
else:
    print(f'{n} é decimal')

