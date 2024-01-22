"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?" X
"Esteve no local do crime?" X
"Mora perto da vítima?" X
"Devia para a vítima?"
"Já trabalhou com a vítima?" 

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""
perguntas = []
pergunta1 = input('Você Telefonou para a vítima?[Sim/Nao]:  ').strip().lower()[0]
if pergunta1 == 's':
    perguntas.append(1)
else:
    perguntas.append(0)
pergunta2 = input('Você esteve no local do crime?[Sim/Nao]: ').strip().lower()[0]

if pergunta2 == 's':
    perguntas.append(1)
else:
    perguntas.append(0)

pergunta3 = input('Você mora perto da vítima?[Sim/Nao]: ').strip().lower()[0]
if pergunta3 == 's':
    perguntas.append(1)
else:
    perguntas.append(0)

pergunta4 = input('Você devia para a vítima?[Sim/Nap]: ').strip().lower()[0]
if pergunta4 == 's':
    perguntas.append(1)
else:
    perguntas.append(0)

pergunta5 = input('Você já trabalhou com a vítima?[Sim/Nao]: ').strip().lower()[0]
if pergunta5 == 's':
    perguntas.append(1)
else:
    perguntas.append(0)
    

total = sum(perguntas)
if total == 2:
    print('Suspeita')
elif total >= 3 and total <= 4:
    print('Cumplice')
elif total == 5:
    print('Assasino')
else:
    print('Inocente')
