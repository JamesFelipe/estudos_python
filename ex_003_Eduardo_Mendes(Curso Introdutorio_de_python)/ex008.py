# Faça um programa que receba uma data de nascimento (15/07/87) e imprima
# 'você nasceu em <dia> de <mês> de <ano>
data = input('Digite sua data de nascimento: ').split('/')
print(f'Você nasceu em {data[0]} de {data[1]} de {data[2]}')
