"""
Desenvolva um programa que armazene quatro notas em uma lista e que apresente a média final.
Caso a média seja igual ou superior a 7, apresentar a mensagem "APROVADO", 
caso contrário, armazenar a nota da prova final e recalcular a média. 
Caso a nova média seja igual superior a 5, apresentar a mensagem "APROVADO", 
caso contrário, apresentar a mensagem "REPROVADO
"""

notas = [10.0, 5.5, 7.5, 10.0]
media = sum(notas) / len(notas)
print(f'Sua média é: {media}')
if media > 5 and media > 7:
    print('Aprovado')
else:
    print('Reprovado')
