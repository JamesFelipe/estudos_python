"""
Faça um programa que leia dez conjuntos de dois valores, 
o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. 
Encontre o aluno mais alto e o mais baixo. 
Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.
"""
# Còdigo Bard
# Programa para encontrar o aluno mais alto e o mais baixo

# Declaração das variáveis
alunos = []
aluno_mais_alto = 0
altura_aluno_mais_alto = 0
aluno_mais_baixo = 0
altura_aluno_mais_baixo = 10000

# Leitura dos dados dos alunos
for i in range(10):
    numero_aluno = int(input("Digite o número do aluno: "))
    altura_aluno = float(input("Digite a altura do aluno: "))
    alunos.append((numero_aluno, altura_aluno))

# Encontra o aluno mais alto
for aluno in alunos:
    if aluno[1] > altura_aluno_mais_alto:
        altura_aluno_mais_alto = aluno[1]
        aluno_mais_alto = aluno[0]

# Encontra o aluno mais baixo
for aluno in alunos:
    if aluno[1] < altura_aluno_mais_baixo:
        altura_aluno_mais_baixo = aluno[1]
        aluno_mais_baixo = aluno[0]

# Print dos resultados
print("O aluno mais alto é o número", aluno_mais_alto, "com altura de", altura_aluno_mais_alto, "cm")
print("O aluno mais baixo é o número", aluno_mais_baixo, "com altura de", altura_aluno_mais_baixo, "cm")
