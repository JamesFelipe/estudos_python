"""
O funcionário chamado Carlos tem um colega chamado João 
que recebe um salário que equivale a um terço do seu salário. 
Carlos gosta de fazer aplicações na caderneta de poupança e vai
aplicar seu salário integralmente nela, pois está rendendo 2% ao mês. 
João aplicará seu salário integralmente no fundo de renda fixa, 
que está rendendo 5% ao mês. 

Construa um programa que deverá calcular e mostrar a quantidade de meses 
necessários para que o valor pertencente a João iguale ou ultrapasse 
o valor pertencente a Carlos. Teste com outros valores para as taxas.
"""
# Código ChatGpt
# Função para calcular o tempo necessário para João igualar ou ultrapassar Carlos
def calcular_meses_para_igualar(salario_carlos, taxa_caderneta, taxa_fundo):
    salario_joao = salario_carlos / 3
    valor_carlos = salario_carlos
    valor_joao = salario_joao
    
    meses = 0
    
    while valor_joao < valor_carlos:
        valor_carlos *= (1 + taxa_caderneta)
        valor_joao *= (1 + taxa_fundo)
        meses += 1
        
    return meses

# Valores iniciais
salario_carlos = float(input("Digite o salário de Carlos: "))
taxa_caderneta = float(input("Digite a taxa de rendimento da caderneta de poupança (em %): ")) / 100
taxa_fundo = float(input("Digite a taxa de rendimento do fundo de renda fixa (em %): ")) / 100

# Calculando a quantidade de meses
meses_necessarios = calcular_meses_para_igualar(salario_carlos, taxa_caderneta, taxa_fundo)

# Mostrando o resultado
print(f"A quantidade de meses necessários para que o valor de João iguale ou ultrapasse o valor de Carlos é: {meses_necessarios}")

