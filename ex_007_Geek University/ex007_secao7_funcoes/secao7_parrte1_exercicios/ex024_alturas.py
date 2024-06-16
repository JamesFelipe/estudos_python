"""
Faça um programa que leia dez conjuntos de dois valores,
o primeiro representando o número do aluno 
e o segundo representando a sua altura em metros. 

Encontre o aluno mais baixo e o mais alto. 
Mostre o número do aluno mais baixo e do mais alto, juntamente
com suas alturas.
"""
# Código ChatGpt
# Inicializando variáveis para armazenar informações do aluno mais baixo e mais alto
aluno_mais_baixo = 0
altura_mais_baixa = float('inf')  # Inicializando com um valor infinito para garantir que qualquer altura seja menor
aluno_mais_alto = 0
altura_mais_alta = 0

# Loop para ler os dados dos alunos
for i in range(1, 11):  # Loop de 1 a 10 para os 10 conjuntos de valores
    numero_aluno = int(input(f"Digite o número do aluno {i}: "))
    altura_aluno = float(input(f"Digite a altura do aluno {i} em metros: "))

    # Verificando se é o aluno mais baixo
    if altura_aluno < altura_mais_baixa:
        aluno_mais_baixo = numero_aluno
        altura_mais_baixa = altura_aluno

    # Verificando se é o aluno mais alto
    if altura_aluno > altura_mais_alta:
        aluno_mais_alto = numero_aluno
        altura_mais_alta = altura_aluno

# Exibindo os resultados
print(f"O aluno mais baixo é o número {aluno_mais_baixo} com altura de {altura_mais_baixa} metros.")
print(f"O aluno mais alto é o número {aluno_mais_alto} com altura de {altura_mais_alta} metros.")
