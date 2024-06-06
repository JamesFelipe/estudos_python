"""
Leia a nota e o número de faltas de um aluno, e escreva seu conceito. De acordo com a
tabela abaixo, quando o aluno tem mais de 20 faltas ocorre uma redução de conceito.

__________________________________________________________________________________
|       Nota         |  Conceito(Até 20 Faltas)  |  Conceito(Mais de 20 Faltas)  |
|   9.0 até 10.0     |      A                    |             B                 |
|   7.5 até 8.9      |      B                    |             C                 |
|   5.0 até 7.4      |      C                    |             D                 |
|   4.0 até 4.9      |      D                    |             E                 |
|   0.0 até 3.9      |      E                    |             E                 |
----------------------------------------------------------------------------------
"""
nota = float(input('Digite sua nota: '))
numero_faltas = int(input('Digite seu número de faltas: '))
if (nota >= 9 and nota >= 10) and numero_faltas <= 20:
    print(f'Conceito A')
elif (nota >= 7.5 and nota <= 8.9) and numero_faltas <= 20:
    print('Conceito B')
elif (nota >= 5.0 and nota <= 7.4) and numero_faltas <= 20:
    print('Conceito C')
elif (nota >= 4.0 and nota <= 4.9) and numero_faltas <= 20:
    print('Conceito D')
elif (nota >= 0.0 and nota <= 3.9) and numero_faltas <= 20:
    print('Conceito E')

if (nota >= 9 and nota >= 10) and numero_faltas >= 20:
    print(f'Conceito B')
elif (nota >= 7.5 and nota <= 8.9) and numero_faltas <= 20:
    print('Conceito C')
elif (nota >= 5.0 and nota <= 7.4) and numero_faltas <= 20:
    print('Conceito D')
elif (nota >= 4.0 and nota <= 4.9) and numero_faltas <= 20:
    print('Conceito E')
else:
    print('Conceito E')
