# Faça um programa que calcule o número médio de alunos por turma. 
# Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. 
# As turmas não podem ter mais de 40 alunos.
print(f'Turmas com mais de 40 alunos serão removidas')
alunos = []
turmas = int(input('Dgite quantas turmas temos: '))
for i in range(1, turmas + 1):
    aluno = int(input(f'Digite quantos alunos temos na turma {i}: '))
    if aluno < 40:
        alunos.append(aluno)
    else:
        print('Valor inválido')
print(f'A média é de {sum(alunos) / turmas} alunos por turma')
