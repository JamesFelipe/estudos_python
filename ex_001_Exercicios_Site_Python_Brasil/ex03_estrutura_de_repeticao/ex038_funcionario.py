"""
Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
    A - Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
    B - Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
    C - A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. 

Faça um programa que determine o salário atual desse funcionário. 
Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.
"""
# Código Bard
# Programa para calcular o salário atual de um funcionário

# Ano atual
ano_atual = 2024

# Digite o salário inicial do funcionário
salario_inicial = float(input("Digite o salário inicial do funcionário: "))

# Aumento salarial de 1996
aumento_1996 = 0.015 * salario_inicial

# Salário do funcionário em 1996
salario_1996 = salario_inicial + aumento_1996

# Anos a partir de 1997
anos_posteriores = ano_atual - 1997

# Aumento salarial anual a partir de 1997
aumento_anual = aumento_1996 * 2

# Salário atual do funcionário
salario_atual = salario_1996 + anos_posteriores * aumento_anual

# Print do salário atual
print("O salário atual do funcionário é de R$", salario_atual)
