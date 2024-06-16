"""
Um funcionário recebe aumento anual. 
Em 1995 foi contratado por 2000 reais. 
Em 1996 recebeu aumento de 1.5%. 
A partir de 1997, os aumentos sempre correspondem ao dobro do ano anterior. 
Faça programa que determine o salário atual do funcionário.
"""
# Qual o erro desse código, pretendo pegar o dobro de porcentos a cada ano
import datetime
ano_atual = datetime.date.today().year

# O ano do primeiro aumento
ano = 1996
salario = 2000
porcentos = 0.015
while ano < ano_atual + 1:
    """
    Essa parte comentada foi corrigida pelo chatGpt  
    porcentos = 0.015
    porcentos *= 2
    aumento = salario + (salario * porcentos/ 100) 
    """
    aumento = salario * porcentos
    salario += aumento
    
    porcentos *= 2
    ano += 1
    
print(f"O salário atual seria de: {aumento:.2f}")
