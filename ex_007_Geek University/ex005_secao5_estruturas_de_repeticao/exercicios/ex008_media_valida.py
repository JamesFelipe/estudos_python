"""
Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas e
exiba na tela a média destas notas. Uma nota válida deve ser, obrigatoriamente, um
valor entre 0.0 e 10.0, onde caso a nota não possua um valor válido, este fato deve ser
informado ao usuário e o programa termina.
"""
nota1 = float(input('Digite sua primeira média: '))
if nota1 > 0 and nota1 <= 10.0:
    print(f'Nota válida adicionada')
    nota2 = float(input('Digite sua segunda nota: '))
    if nota2 > 0  and nota2 <= 10.0:
        print('Nota válida adicionada')
        media = (nota1 + nota2) / 2
        print(f'Sua média é: {media}')
    else:
        print('Nota inválida, Programa encerrado')
else:
    print('Nota inválida, Programa encerrado')    
