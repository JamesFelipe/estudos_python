"""
Faça um programa para a leitura de duas notas parciais de um aluno. 
O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
media = (nota1 + nota2) / 2
if media == 10:
    print(f'Nota: {media:.2f} - Aprovado com distinção')
elif media >= 7:
    print(f'Nota: {media:.2f} - Aprovado')
else:
    print(f'Nota: {media:.2f} - Reprovado')
