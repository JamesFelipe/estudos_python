"""
Faça um programa para ler a nota da prova de 15 alunos e armazene num vetor, calcule
e imprima a média geral.
"""
notas = []
for i in range(1, 16):
    nota = float(input(f'Digite a {i}ª nota: '))
    notas.append(nota)

print(f'A nota geral é: {sum(notas) / len(notas)}')
