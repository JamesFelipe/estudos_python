"""
Faça um Programa para um caixa eletrônico. 

O programa deverá perguntar ao usuário a valor do saque 
e depois informar quantas notas de cada valor serão fornecidas.
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a quantidade de
notas existentes na máquina.

Exemplo 1: Para sacar a quantia de 256 reais,
o programa fornece duas notas de 100, uma nota de 50,
uma nota de 5 e uma nota de 1;

Exemplo 2: Para sacar a quantia de 399 reais,
o programa fornece três notas de 100, uma nota de 50, 
quatro notas de 10, uma nota de 5 e quatro notas de 1.
"""
# Código ChatGpt
valor_saque = int(input("Digite o valor do saque: "))

# Verifica se o valor está dentro do intervalo permitido
if valor_saque < 10 or valor_saque > 600:
    print("O valor deve ser entre 10 e 600 reais.")
else:
    notas = [100, 50, 10, 5, 1]  # Notas disponíveis
    distribuicao = {}

    # Calcula a quantidade de cada nota
    for nota in notas:
        quantidade_notas = valor_saque // nota
        if quantidade_notas > 0:
            distribuicao[nota] = quantidade_notas
        valor_saque %= nota  # Atualiza o valor a ser sacado

    # Exibe as notas fornecidas
    print("Notas fornecidas:")
    for nota, quantidade in distribuicao.items():
        print(f"{quantidade} nota(s) de {nota} reais")
