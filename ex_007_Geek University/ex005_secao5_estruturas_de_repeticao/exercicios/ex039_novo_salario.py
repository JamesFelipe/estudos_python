"""
Uma empresa decide dar um aumento aos seus funcionários de acordo com uma tabela
que considera o salário atual e o tempo de serviço de cada funcionário. 
Os funcionários com menor salário terão um aumento proporcionalmente maior do que os funcionários
com um salário maior, e conforme o tempo de serviço na empresa, cada funcionário irá
receber um bônus adicional de salário. Faça um programa que leia:
    * o valor do salário atual do funcionário;
    * O tempo de serviço desse funcionário na empresa (número de anos de trabalho na
    empresa).
    
Use as tabelas abaixo para calcular o salário reajustado deste funcionário e imprima o
valor do salário final reajustado, ou uma mensagem caso o funcionário não tenha direito
a nenhum aumento.
_______________________________________________________________________________
|   Salário Atual         |Reajuste(%)     | Tempo de Serviço   | Bônus       |
|       Até 500,00        |   25%           |   Abaixo de 1 ano |   Sem bônus |
|       Até 1000,00)      |   20%           |   De 1 a 3 anos   |   100,00    |
|       Até 1500,00)      |   15%           |   De 4 a 6 anos   |   200,00    |
|       Até 2000,00)      |   10%           |   De 7 a 10 anos  |   300,00    |
|       Acima de 2000,00  |   Sem reajuste  |   Mais de 10 anos |   500,00    |
-------------------------------------------------------------------------------
"""
salario = float(input('Digite o valor do seu salário: '))
tempo_servico = float(input('Digite quanto tempo você tem de anos na empresa: '))
if salario <= 500 and tempo_servico <= 1:
    reajuste = salario + (salario * 25/100)
    print(f'Seu noo salário será de {reajuste:.2f} R$, você não tem direito a bônus')
elif salario <= 1_000 and tempo_servico > 1 and tempo_servico <= 3:
    reajuste = salario + (salario * 20/100)
    print(f'Seu noo salário será de {reajuste + 100:.2f} R$, incluído 100 de bônus')
elif salario <= 1_500 and tempo_servico > 4 and tempo_servico <= 6:
    reajuste = salario + (salario * 15/100)
    print(f'Seu noo salário será de {reajuste + 200:.2f} R$, incluído 200 de bônus')
elif salario <= 2_000 and tempo_servico > 7 and tempo_servico <= 10:
    reajuste = salario + (salario * 1/100)
    print(f'Seu noo salário será de {reajuste + 300:.2f} R$, incluído 300 de bônus')
elif salario >= 2_000 and tempo_servico >= 10:
    print(f'Seu noo salário será de com bônus de 500 reais será: {salario + 500} R$')
