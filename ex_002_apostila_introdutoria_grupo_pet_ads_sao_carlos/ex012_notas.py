# Escreva um programa que leia 10 notas e informe a média dos alunos.
notas = []
for i in range(1, 11):
    nota = float(input(f'Digite a {i}ª nota: '))
    notas.append(nota)
print(f'A média das notas é: {sum(notas) / len(notas)}')
