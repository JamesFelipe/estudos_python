"""
Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar

A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.
"""

nota1 = float(input('Digite sua primeira nota> '))
nota2 = float(input('Digite sua segunda nota> '))
nota3 = float(input('Digite sua terceira nota> '))
media = (nota1 + nota2 + nota3) / 3
if media == 10:
    print(f'Sua média foi: {media:.1f}, você foi Aprovado com Distinção!')
elif media >= 7:
    print(f'Sua média foi: {media:.1f}, Você foi Aprovado!')
elif media < 7:
    print(f'Sua média foi {media:.1f}, você foi Reprovado!')
