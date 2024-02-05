"""
 Faça um programa para a leitura de duas notas parciais de um aluno.
 O programa deve calcular a média alcançada por aluno e apresentar
 a mensagem "Aprovado", se a média for maior ou igual a sete
 a mensagem "Reprovado", se a média for menor que sete
 a mensagem aprovado com distinção, se a média for igual a dez"""
nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('DIgite a 2ª nota: '))
media = (nota1 + nota2) / 2
if media >= 10:
    print('Aprovado com distinção')
elif media < 10 and media >= 7:
    print('Aprovado') 
elif media < 7:
    print('Reprodvado')
