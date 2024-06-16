"""
Chico tem 1.50 metro e cresce 2 centímetros por ano, 
enquanto Zé tem 1.10 metros e cresce 3 centímetros por ano. 
Escreva um programa que calcule e imprima quantos anos serão 
necessários para que Zé seja maior que Chico.
"""
# Código ChatGpt
# Alturas iniciais de Chico e Zé
altura_chico = 1.50
altura_ze = 1.10

# Taxas de crescimento por ano
crescimento_chico = 0.02  # 2 centímetros por ano
crescimento_ze = 0.03     # 3 centímetros por ano

# Contador de anos
anos = 0

# Loop até que Zé seja mais alto que Chico
while altura_ze <= altura_chico:
    altura_chico += crescimento_chico
    altura_ze += crescimento_ze
    anos += 1

# Resultado
print(f"Serão necessários {anos} anos para que Zé seja maior que Chico.")
