"""
Faça um algoritmo que calcule a média ponderada das notas de 3 provas. A primeira e
a segunda prova têm peso 1 e a terceira tem peso 2. Ao final, mostrar a média do aluno
e indicar se o aluno foi aprovado ou reprovado. A nota para aprovação deve ser igual ou
superior a 60 pontos.
"""
prova1 = float(input('Digite o valor da primeira prova: '))
prova2 = float(input('Digite o valor da terceira prova: '))
prova3 = float(input('Digite o valor da terceira prova: '))
media = (prova1 * 1 + prova2 * 1 + prova3 * 2) / (1 + 1 + 2)
if media >= 6.0:
    print(f'Média: {media:.2f}, Aluno Aprovado')
else:
    print(f'Média: {media}, Aluno Reprovado')
